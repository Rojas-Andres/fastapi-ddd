from typing import Callable, Optional

from app.domain.base_domain.service_layer import messagebus
from app.domain.base_domain.service_layer.unit_of_work import AbstractUnitOfWork
from app.infrastructure.messaging import handlers
from app.modules.auth.adapters.unit_of_work import AuthUnitOfWork
from app.shared.auth.auth_class import TokenHandler
from app.shared.auth.jwt_handler import JWTToken

MODULE_NAME = "AUTH"


def bootstrap(
    uow: Optional[AbstractUnitOfWork] = None,
    token_handler: Optional[TokenHandler] = None,
    publish: Optional[Callable] = None,
    # notify: Optional[AbstractNotification] = None,
) -> messagebus.MessageBus:
    uow = uow or AuthUnitOfWork()
    publish = publish or handlers.publish_async
    # notify = notify or EmailNotification()
    token_handler = token_handler or JWTToken()
    event_handlers, command_handlers = messagebus.load_handlers(MODULE_NAME)
    return messagebus.create_messagebus(
        uow=uow,
        event_handlers=event_handlers,
        command_handlers=command_handlers,
        dependencies={
            "uow": uow,
            "token_handler": token_handler,
            "publish": publish,
            # "notify": notify,
        },
    )
