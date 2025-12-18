import pytest

from businesses.business import UserService
from impls.fake import FakeUserRepo
from impls.impl import ImplUserRepo
from impls.broken import BrokenUserRepo


def test_greet_with_fake_repo():
    """DIにより、RepoをFakeに差し替えるだけでBusinessを単体テストできる"""

    # もし、business.pyで具象のImplUserRepoを直接使っていたら(newしていたら)、FakeUserRepoに差し替えた場合のテストはできなくなってしまう。
    service = UserService(FakeUserRepo())
    assert service.greet(999) == "Hello, TEST_USER!"


def test_greet_with_impl_repo_success():
    """Implでもテスト可能。DBの代わりにdictを渡して純粋関数っぽくできる"""
    repo = ImplUserRepo({1: "Ada"})
    service = UserService(repo)
    assert service.greet(1) == "Hello, Ada!"


def test_greet_with_impl_repo_missing_user_raises_keyerror():
    """Repo側の仕様が例外なら、それもテストできる（ここでは KeyError）"""
    repo = ImplUserRepo({1: "Ada"})
    service = UserService(repo)

    with pytest.raises(KeyError):
        service.greet(2)


def test_broken_repo_cannot_be_instantiated():
    """
    ABC + abstractmethod により、契約違反のRepoは注入以前に弾かれる
    → “壊れた実装が紛れ込む”のを早期に検出できる
    """
    with pytest.raises(TypeError):
        BrokenUserRepo()

#--------------

from businesses.business import UserService
from abstracts.abstract import AbstractUserRepo

# Stubパターンによる振る舞い検証の例(固定値を返すだけだから)
def test_greet_with_inline_virtual_repo():
    """
    implsに存在しない“仮想Repo”をテスト内で定義して注入できる。
    → businessの単体テストがRepo都合から独立できる、というDI/DIPの旨味。
    """

    class VirtualRepo(AbstractUserRepo):
        def get_name(self, user_id: int) -> str:
            return f"VIRTUAL-{user_id}"

    service = UserService(VirtualRepo())
    assert service.greet(42) == "Hello, VIRTUAL-42!"


#--------------
# Spyパターンによる振る舞い検証の例(Spyとして、「関数をちゃんと呼んだか、呼ばれた事実を記録する」)
# UserService が repo.get_name をちゃんと呼んだか」を確認する例で
from businesses.business import UserService
from abstracts.abstract import AbstractUserRepo


def test_greet_calls_repo_with_expected_user_id():
    class SpyRepo(AbstractUserRepo):
        def __init__(self) -> None:
            self.called_with: list[int] = []

        def get_name(self, user_id: int) -> str:
            self.called_with.append(user_id)
            return "SPY"

    repo = SpyRepo()
    service = UserService(repo)

    assert service.greet(7) == "Hello, SPY!"
    assert repo.called_with == [7]


#------------
# Mockパターンによる振る舞い検証の例(Mockとして、「関数をちゃんと呼んだか、呼ばれた事実を検証する」)
from businesses.business import UserService


def test_with_mock_repo_using_pytest_mock(mocker):
    # Mockオブジェクトを作成
    repo = mocker.Mock()
    repo.get_name.return_value = "MOCK"

    service = UserService(repo)
    result = service.greet(1)

    assert result == "Hello, MOCK!"
    repo.get_name.assert_called_once_with(1)
