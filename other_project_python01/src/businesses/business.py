

from abstracts.abstract import AbstractUserRepo

class UserService:
    def __init__(self, repo: AbstractUserRepo):
        self._repo = repo  # ← 具象じゃなく抽象(AbstractUserRepo)のインスタンスが来ることを期待し、受け取る

    def greet(self, user_id: int) -> str:
        name = self._repo.get_name(user_id)
        return f"Hello, {name}!"
