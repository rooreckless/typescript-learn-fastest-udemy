from abstracts.abstract import AbstractUserRepo

# これはわざと、AbstractUserRepoを正しく実装していないクラス
class BrokenUserRepo(AbstractUserRepo):
    def get_age(self, user_id: int) -> str:
        return "20"
