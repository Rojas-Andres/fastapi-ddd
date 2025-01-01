from celery.schedules import crontab

from app.infrastructure.messaging.constants import (
    LOCAL_BROKER_URL,
    LOCAL_TASKS_QUEUE_URL,
)
from app.shared.utils.config.settings import settings

task_serializer = "pickle"
accept_content = ["json", "pickle"]
enable_utc = True
timezone = "UTC"
task_track_started = True
broker_url = LOCAL_BROKER_URL

broker_transport_options = {
    "predefined_queues": {
        settings.QUEUES_NAMES.QUEUE_DEFAULT: {"url": LOCAL_TASKS_QUEUE_URL},
    }
}

beat_schedule = {
    "task_example": {
        "task": "task_example",
        "schedule": crontab(minute="*"),
        "relative": True,
    },
}
