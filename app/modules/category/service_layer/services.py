from app.core.exceptions import ObjectNotFoundException
from app.modules.category.domain.repository import AbstractCategoryUnitOfWork


class GetAllCategorys:
    def __init__(
        self,
        uow: AbstractCategoryUnitOfWork,
    ):
        self.uow = uow

    def get(self):
        with self.uow:
            categorys = self.uow.category.get_categorys()
            return categorys


class CreateCategory:
    def __init__(
        self,
        uow: AbstractCategoryUnitOfWork,
    ):
        self.uow = uow

    def create(self, name: str):
        with self.uow:
            new_category = self.uow.category.create_category(name=name)
            self.uow.commit()
            return new_category


class GetSingleCategory:
    def __init__(
        self,
        uow: AbstractCategoryUnitOfWork,
    ):
        self.uow = uow

    def get(self, category_id: int):
        with self.uow:
            category = self.uow.category.get_category_by_id(category_id)
            if not category:
                raise ObjectNotFoundException("Category not found")
            return category
