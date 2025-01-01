from inspect import getmro
from typing import Any, Callable, Optional, Type

from app.domain.base_domain.domain.message import Command, Event
from app.shared.exceptions import ExceptionMapper
from app.shared.tools import import_string


def empty_handler(*args, **kwargs):
    pass


def apply_async(func_name: str) -> Callable:
    return lambda message, publish: publish(func_name, message)


def settings_handlers(
    sync_handlers: Optional[dict[str, list[str] | str]] = None,
    async_handlers: Optional[dict[str, list[str] | str]] = None,
) -> dict:
    """
    Helper function that provides a proxy between the global handlers vs the
    client handlers.

    # global_settings.py
    >>> SPECIFIC_DOMAIN_HANDLERS = {}

    # settings.py
    >>> SPECIFIC_DOMAIN_HANDLERS = {
    ...     "path.CommandClass": "path.callable.command",
    ...     "path.EventClass": ["path.event.callable", "task_name"],
    ... }
    # At execution
    >>> from app.shared.utils.config.settings import settings
    >>> settings_handlers(settings.SPECIFIC_DOMAIN_HANDLERS)
    ... {
    ...    CommandClass: command_callable,
    ...    EventClass: [event_callable, apply_async("task_name")]
    ... }

    Returns:
        A dict with the Callable for each Message

    Raises:
        ImproperlyConfigured: When the handlers for the Message are not well
            stablished or when the path for the handlers are broken.
    """

    handlers: dict = {}
    async_handlers = async_handlers or {}
    sync_handlers = sync_handlers or {}

    for message_path, handlers_path in sync_handlers.items():
        handlers |= _get_handlers(message_path, handlers_path)

    for message_path, task_name in async_handlers.items():
        handlers |= _get_handlers(message_path, task_name, is_async=True)

    return handlers


def _get_handlers(
    message_path: str,
    handlers_path: list[str] | str,
    is_async: Optional[bool] = False,
) -> dict:
    message = _import_string(message_path)
    _validate_handlers(message, handlers_path)
    func = apply_async if is_async else _import_string

    if isinstance(handlers_path, str):
        return {message: func(handlers_path)}

    imported_handlers = [func(path) for path in handlers_path]

    return {message: imported_handlers}


def _validate_handlers(message: Any, handlers: list[str] | str) -> None:
    if not isinstance(handlers, str) and Command in getmro(message):
        raise ExceptionMapper(f"The Command {message} can only have a unique handler")
    elif not isinstance(handlers, list) and Event in getmro(message):
        raise ExceptionMapper(f"The Event {message} needs a list of handlers")
    elif not (Command in getmro(message) or Event in getmro(message)):
        raise ExceptionMapper(f"The message {message} isn't a Command or an Event")


def _import_string(path: str) -> Type[Command] | Type[Event] | Callable:
    try:
        return import_string(path)
    except ImportError as exec_info:
        raise ExceptionMapper(str(exec_info))
