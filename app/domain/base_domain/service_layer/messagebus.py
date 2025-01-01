import inspect
import logging
from queue import Queue
from typing import Any, Callable, Type

from tenacity import RetryError, Retrying, stop_after_attempt, wait_exponential

from app.domain.base_domain.domain.message import Command, Event, Message
from app.domain.base_domain.messaging.handlers import settings_handlers
from app.domain.base_domain.service_layer import unit_of_work
from app.shared.utils.config.settings import settings

logger = logging.getLogger(__name__)


class MessageBus:
    def __init__(
        self,
        uow: unit_of_work.AbstractUnitOfWork,
        event_handlers: dict[Type[Event], list[Callable]],
        command_handlers: dict[Type[Command], Callable],
    ):
        self.uow = uow
        self.event_handlers = event_handlers
        self.command_handlers = command_handlers
        self.queue: Queue = Queue()

    def handle(self, message: Message) -> list[Any]:
        results = []
        self.queue.put(message)
        while not self.queue.empty():
            message = self.queue.get()
            if isinstance(message, Event):
                self.handle_event(message)
            elif isinstance(message, Command):
                cmd_result = self.handle_command(message)
                results.append(cmd_result)
            else:
                raise Exception(f"{message} was not an Event or Command")
        return results

    def handle_event(self, event: Event):
        for handler in self.event_handlers[type(event)]:
            try:
                for attempt in Retrying(
                    stop=stop_after_attempt(settings.DEFAULT_RETRY_ATTEMPTS),
                    wait=wait_exponential(),
                ):
                    with attempt:
                        logger.debug(f"handling event {event} with handler {handler}")
                        handler(event)
                        list(map(self.queue.put, self.uow.collect_new_events()))
            except RetryError as retry_failure:
                logger.error(
                    f"Exception handling event {event}:"
                    f" {str(retry_failure.last_attempt.exception())}"
                )

    def handle_command(self, command: Command):
        logger.debug(f"handling command {command}")
        try:
            handler = self.command_handlers[type(command)]
            result = handler(command)
            list(map(self.queue.put, self.uow.collect_new_events()))
            return result
        except Exception:
            logger.exception(f"Exception handling command {command}")
            raise


def create_messagebus(
    uow: unit_of_work.AbstractUnitOfWork,
    event_handlers: dict[Type[Event], list[Callable]],
    command_handlers: dict[Type[Command], Callable],
    dependencies: dict[str, Any],
) -> MessageBus:
    injected_event_handlers = {
        event_type: [_inject(handler, dependencies) for handler in event_handlers]
        for event_type, event_handlers in event_handlers.items()
    }
    injected_command_handlers = {
        command_type: _inject(handler, dependencies)
        for command_type, handler in command_handlers.items()
    }
    return MessageBus(
        uow=uow,
        event_handlers=injected_event_handlers,
        command_handlers=injected_command_handlers,
    )


def _inject(handler: Callable, dependencies: dict[str, Any]) -> Callable:
    params = inspect.signature(handler).parameters
    deps = {
        name: dependency for name, dependency in dependencies.items() if name in params
    }
    return lambda message: handler(message, **deps)


def load_handlers(module: str) -> tuple[dict, dict]:
    event_handlers = settings_handlers(
        getattr(settings, f"{module}_EVENT_HANDLERS"),
        getattr(settings, f"{module}_EVENT_ASYNC_HANDLERS"),
    )
    command_handlers = settings_handlers(
        getattr(settings, f"{module}_COMMAND_HANDLERS"),
        getattr(settings, f"{module}_COMMAND_ASYNC_HANDLERS"),
    )

    return event_handlers, command_handlers
