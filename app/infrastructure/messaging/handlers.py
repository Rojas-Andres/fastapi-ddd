from dataclasses import asdict
from typing import Callable

from celery.result import AsyncResult

from app.domain.base_domain.domain.message import Message
from app.infrastructure.messaging.app import task_manager
from app.shared.tools import import_string
from app.shared.utils.config.settings import ImproperlyConfigured, settings


def publish_async(task_name: str, message: Message) -> AsyncResult:
    kwargs = {"event_name": message.__class__.__name__, **asdict(message)}
    options = {"queue": settings.MANAGEMENT_QUEUE[task_name]}

    return task_manager.send_task(task_name, kwargs=kwargs, **options)


def import_settings_tasks(settings_tasks: dict[str, str]) -> dict[str, Callable]:
    """Helper function that provides a proxy between the global tasks vs the
    host tasks.

    # global_settings.py
    >>> SPECIFIC_DOMAIN_TASKS = {}
    # manage_settings.py
    >>> SPECIFIC_DOMAIN_TASKS = {"task_name": "path.callable"}
    # At execution
    >>> from app.shared.utils.config.settings import settings
    >>> import_settings_tasks(settings.SPECIFIC_DOMAIN_TASKS)
    ... {
    ...    "task_name": task_callable,
    ... }

    Returns:
        A dict with the Callable for each Task

    Raises:
        ImproperlyConfigured: When the tasks for the Task are not well
            stablished or when the path for the tasks are broken.
    """
    try:
        imported_tasks = {
            name: import_string(path) for name, path in settings_tasks.items()
        }
    except ImportError as exec_info:
        raise ImproperlyConfigured(str(exec_info))

    return imported_tasks
