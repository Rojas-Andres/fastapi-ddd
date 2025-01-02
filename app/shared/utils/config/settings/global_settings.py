import os
from collections import defaultdict
from os import getenv

from app.infrastructure.messaging.constants import QueueName

####################
# GENERAL SETTINGS #
####################
ENVIRONMENT = os.getenv("ENVIRONMENT", "develop")
PROJECT_NAME = os.getenv("PROJECT_NAME", "fastapi_stack")
DEFAULT_RETRY_ATTEMPTS = 3
MANAGEMENT_QUEUE: dict[str, str] = defaultdict(lambda: QUEUES_NAMES.QUEUE_DEFAULT)

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
    f"{auth_path}.domain.commands.AuthenticateUser": f"{auth_path}.service_layer.handlers.login_user",
    # f"{auth_path}.domain.commands.ExampleCommandTask": f"{auth_path}.service_layer.handlers.example_test",
}

AUTH_COMMAND_ASYNC_HANDLERS: dict[str, str] = {}
AUTH_EVENT_ASYNC_HANDLERS: dict[str, str] = {
    f"{auth_path}.domain.events.UserCreated": [
        "task_new_user_notification",
    ],
}
# ASYNC TASKS
AUTH_ASYNC_TASKS: dict[str, str] = {
    "task_new_user_notification": f"{auth_path}.tasks.task_new_user_notification",
    # "task_example": f"{auth_path}.tasks.task_example",
}

AUTH_EVENT_HANDLERS: dict[str, str] = {
    f"{auth_path}.domain.events.NewUserNotification": [
        f"{auth_path}.service_layer.handlers.new_user_notification"
    ],
}

user_path = "app.modules.user"

USER_COMMAND_HANDLERS: dict[str, str] = {
    f"{user_path}.domain.commands.ChangePasswordUser": f"{user_path}.service_layer.handlers.change_password_user",
}

USER_COMMAND_ASYNC_HANDLERS: dict[str, str] = {}
USER_EVENT_ASYNC_HANDLERS: dict[str, str] = {}
# ASYNC TASKS
USER_ASYNC_TASKS: dict[str, str] = {}

USER_EVENT_HANDLERS: dict[str, str] = {}


# ########################
# ASYNC TASKS QUEUE
QUEUES_NAMES = QueueName
ASYNC_TASKS |= AUTH_ASYNC_TASKS
