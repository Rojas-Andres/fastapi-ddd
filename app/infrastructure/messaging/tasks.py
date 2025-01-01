from app.infrastructure.messaging.app import task_manager
from app.infrastructure.messaging.handlers import import_settings_tasks
from app.shared.utils.config.settings import settings

ASYNC_TASKS = import_settings_tasks(settings.ASYNC_TASKS)

[task_manager.task(func, name=name) for name, func in ASYNC_TASKS.items()]
