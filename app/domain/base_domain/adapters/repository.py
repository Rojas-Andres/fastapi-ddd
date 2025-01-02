# import abc
# from typing import Any, Generic, Optional, Type, TypeVar

# # from django.db import models

# _M = TypeVar("_M")


# # class AbstractRepository(abc.ABC, Generic[_M]):
# #     model: Type[models.Model]

# #     def __init__(self):
# #         self.seen = set()


# class AbstractReadRepository(AbstractRepository, Generic[_M]):
#     @abc.abstractmethod
#     def get(self, id: Any) -> Optional[_M]:
#         raise NotImplementedError

#     @abc.abstractmethod
#     def to_domain(self, orm: Any) -> _M:
#         raise NotImplementedError
