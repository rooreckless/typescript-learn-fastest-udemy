from abstracts.abstract import AbstractUserRepo

class FakeUserRepo(AbstractUserRepo):
    def get_name(self, user_id: int) -> str:
        return "TEST_USER"
