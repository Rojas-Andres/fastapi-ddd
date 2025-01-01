import os
from collections import defaultdict
from datetime import timedelta
from enum import Enum
from os import getenv
from typing import Any

from app.infrastructure.messaging.constants import QueueName

####################
# GENERAL SETTINGS #
####################
ENVIRONMENT = os.getenv("ENVIRONMENT", "develop")
PROJECT_NAME = os.getenv("PROJECT_NAME", "fastapi_stack")
DEFAULT_RETRY_ATTEMPTS = 3

ASYNC_TASKS: dict[str, str] = {}

DYNAMODB_INGRESS_API_LOG_TABLE_NAME = getenv(
    "DYNAMODB_INGRESS_API_LOG_TABLE_NAME", "ingress_api_log"
)

DYNAMODB_EGRESS_API_LOG_TABLE_NAME = getenv(
    "DYNAMODB_EGRESS_API_LOG_TABLE_NAME", "egress_api_log"
)

auth_path = "app.modules.auth"

AUTH_COMMAND_HANDLERS: dict[str, str] = {
    f"{auth_path}.domain.commands.CreateUser": f"{auth_path}.service_layer.handlers.create_user",
    # f"{auth_path}.domain.commands.ExampleCommandTask": f"{auth_path}.service_layer.handlers.example_test",
}

AUTH_COMMAND_ASYNC_HANDLERS: dict[str, str] = {}
AUTH_EVENT_ASYNC_HANDLERS: dict[str, str] = {
    # f"{auth_path}.domain.events.UserCreated": [
    #     "task_new_auth_notification",
    # ],
}
# ASYNC TASKS
AUTH_ASYNC_TASKS: dict[str, str] = {
    "task_new_auth_notification": f"{auth_path}.tasks.task_new_auth_notification",
    # "task_example": f"{auth_path}.tasks.task_example",
}

AUTH_EVENT_HANDLERS: dict[str, str] = {
    # f"{auth_path}.domain.events.NewUserNotification": [
    #     f"{auth_path}.service_layer.handlers.new_AUTH_notification"
    # ],
}
# ########################
# ASYNC TASKS QUEUE
QUEUES_NAMES = QueueName
ASYNC_TASKS |= AUTH_ASYNC_TASKS
