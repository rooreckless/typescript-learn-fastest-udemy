from abc import ABC, abstractmethod
# 「implsのクラスは、この抽象クラスを継承し、get_nameメソッドを実装しなければならない。」というbusiness.pyからの契約
class AbstractUserRepo(ABC):
    @abstractmethod
    def get_name(self, user_id: int) -> str: ...
