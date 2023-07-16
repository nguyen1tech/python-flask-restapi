import abc

from main import db
from main.models.user import User
from main.shared.sql_result import InsertResult, DeleteResult


class UserRepository:

    @abc.abstractmethod
    def get_by_username(self, username: str):
        raise NotImplementedError

    @abc.abstractmethod
    def create(self, user: User) -> InsertResult:
        raise NotImplementedError

    @abc.abstractmethod
    def delete(self, username: str) -> DeleteResult:
        raise NotImplementedError


def _save_changes(user: User) -> None:
    db.session.add(user)
    db.session.commit()


class SqlUserRepository(UserRepository):

    def get_by_username(self, username: str) -> User:
        return User.query.filter_by(username=username).first()

    def create(self, user: User) -> InsertResult:
        _save_changes(user)
        return InsertResult(inserted=1, exists=False)

    def delete(self, username: str) -> DeleteResult:
        pass
