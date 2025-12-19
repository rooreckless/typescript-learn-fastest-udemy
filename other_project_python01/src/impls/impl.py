from abstracts.abstract import AbstractUserRepo
class ImplUserRepo(AbstractUserRepo):
    def __init__(self, data: dict[int, str]):
        self._data = data

    def get_name(self, user_id: int) -> str:
        return self._data[user_id]
