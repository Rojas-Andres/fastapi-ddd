from app.modules.auth import bootstrap
from app.modules.auth.domain import events


def task_new_user_notification(user_id: str, *args, **kwargs) -> None:
    event = events.NewUserNotification(user_id)
    bus = bootstrap.bootstrap()
    bus.handle(event)
