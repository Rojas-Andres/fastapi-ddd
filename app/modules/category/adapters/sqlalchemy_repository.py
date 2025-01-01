from sqlalchemy.orm import Session

from app.infrastructure.database.models import CategoryORM
from app.modules.category.domain.repository import AbstractCategoryRepository


class CategorySqlAlchemyRepository(AbstractCategoryRepository):
    def __init__(self, session):
        super().__init__()
        self.session: Session = session

    def get_categorys(self) -> list[dict]:
        return [
            self.to_dict(Category) for Category in self.session.query(CategoryORM).all()
        ]

    def create_category(
        self,
        name: str,
    ) -> dict:
        category = CategoryORM(name=name)
        self.session.add(category)
        self.session.flush()
        return self.to_dict(category)

    def get_category_by_id(self, category_id: int) -> dict:
        category = self.session.query(CategoryORM).filter_by(id=category_id).first()
        return self.to_dict(category) if category else None

    def to_dict(self, category: CategoryORM) -> dict:
        return {
            "id": category.id,
            "name": category.name,
        }
