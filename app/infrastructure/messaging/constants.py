import os

from app.shared.enum import StrEnum

LOCAL_TASKS_QUEUE_URL = os.environ.get("LOCAL_TASKS_QUEUE_URL")
LOCAL_TASKS_QUEUE_FIFO_URL = os.environ.get("LOCAL_TASKS_QUEUE_FIFO_URL")
LOCAL_BROKER_URL = os.environ.get("BROKER_URL", "sqs://")


class QueueName(StrEnum):
    QUEUE_DEFAULT: str = "celery"
    QUEUE_FIFO: str = "celery.fifo"
