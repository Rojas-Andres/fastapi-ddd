import abc

from app.infrastructure.database.db import DEFAULT_SESSION_FACTORY
from app.domain.base_domain.domain import message


class AbstractUnitOfWork(abc.ABC):
    """
    Abstract base class for a Unit of Work pattern.

    This class defines the interface for a Unit of Work, which is responsible for
    managing transactions. It ensures that all operations within a transaction
    are either committed or rolled back as a single unit.

    Methods:
        __enter__() -> AbstractUnitOfWork:
            Enter the runtime context related to this object.

        __exit__(*args):
            Exit the runtime context related to this object and roll back the transaction.

        commit():
            Commit the transaction by calling the _commit method.

        _commit():
            Abstract method to be implemented by subclasses to define the commit logic.

        rollback():
            Abstract method to be implemented by subclasses to define the rollback logic.
    """

    def __init__(self):
        self.events: list[message.Event] = []

    def __enter__(self) -> "AbstractUnitOfWork":
        return self

    def __exit__(self, *args):
        self.rollback()

    def commit(self):
        self._commit()

    def collect_new_events(self):
        while self.events:
            yield self.events.pop(0)

    def add_event(self, event: message.Event | list[message.Event]) -> None:
        if isinstance(event, list):
            self.events.extend(event)
        else:
            self.events.append(event)

    @abc.abstractmethod
    def _commit(self):
        raise NotImplementedError

    @abc.abstractmethod
    def rollback(self):
        raise NotImplementedError


class SqlAlchemyUnitOfWork(AbstractUnitOfWork):
    """
    SqlAlchemyUnitOfWork is a unit of work implementation using SQLAlchemy for managing database transactions.

    Attributes:
        session_factory (Callable): A factory function to create new SQLAlchemy sessions.

    Methods:
        __enter__(): Initializes a new SQLAlchemy session and enters the runtime context.
        __exit__(*args): Closes the SQLAlchemy session and exits the runtime context.
        _commit(): Commits the current transaction.
        rollback(): Rolls back the current transaction.
    """

    def __init__(self, session_factory=DEFAULT_SESSION_FACTORY):
        self.session_factory = session_factory

    def __enter__(self):
        self.session = self.session_factory()  # type: Session
        return super().__enter__()

    def __exit__(self, *args):
        super().__exit__(*args)
        self.session.close()

    def _commit(self):
        self.session.commit()

    def rollback(self):
        self.session.rollback()
