from typing import Callable, Optional

from app.domain.base_domain.service_layer import messagebus
from app.domain.base_domain.service_layer.unit_of_work import AbstractUnitOfWork
from app.infrastructure.messaging import handlers
from app.modules.user.adapters.unit_of_work import UserUnitOfWork
from app.shared.auth.auth_class import HasherAbstract
from app.shared.auth.hasher import Hasher

MODULE_NAME = "USER"


def bootstrap(
    uow: Optional[AbstractUnitOfWork] = None,
    publish: Optional[Callable] = None,
    hasher_handler: Optional[HasherAbstract] = None,
    # notify: Optional[AbstractNotification] = None,
) -> messagebus.MessageBus:
    uow = uow or UserUnitOfWork()
    publish = publish or handlers.publish_async
    hasher_handler = hasher_handler or Hasher()
    event_handlers, command_handlers = messagebus.load_handlers(MODULE_NAME)
    return messagebus.create_messagebus(
        uow=uow,
        event_handlers=event_handlers,
        command_handlers=command_handlers,
        dependencies={
            "uow": uow,
            "hasher": hasher_handler,
            "publish": publish,
            # "notify": notify,
        },
    )
