from ..models.user import User
from ..repositories.user import UserRepository
from ..shared.sql_result import InsertResult


class UserService:

    def __init__(self, user_repository: UserRepository):
        self.user_repository = user_repository

    def create_user(self, username: str, password: str) -> InsertResult:
        if self.user_repository.get_by_username(username):
            return InsertResult(inserted=0, exists=True)

        user = User(username=username, password=password)
        return self.user_repository.create(user)

    def get_by_username(self, username: str) -> User:
        return self.user_repository.get_by_username(username)
