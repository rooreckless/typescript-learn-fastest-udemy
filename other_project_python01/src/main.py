# 例1 使えるmain.py (ImplUserRepoを使う場合)

from businesses.business import UserService
from impls.impl import ImplUserRepo

def main() -> None:
    repo = ImplUserRepo({1: "Ada", 2: "Taro"}) # ← 具象のimplを生成
    service = UserService(repo)  # businessを作成する ← ここがDI（注入）businessインスタンス作成時に引数に具象implを渡してる。
    # ↑ 「business.pyはAbstractUserRepoに従うimplを受け取ることをコンストラクタで期待」しているが、「ImplUserRepoはAbstractUserRepoを継承している」ので↑のrepoはそれを満たしている。
    print(service.greet(1))
    print(service.greet(2))

if __name__ == "__main__":
    main()

#------------

# # 例2 使えるmain.py (FakeUserRepoを使う場合)
# from businesses.business import UserService
# from impls.fake import FakeUserRepo

# def main() -> None:
#     service = UserService(FakeUserRepo()) # ← ここがDI（注入）↑とは別のimplを渡しているが、FakeUserRepoもAbstractUserRepoに従うimplだから。
#     #↑ 「businessで違うimplを使いたい」がためにbusinessを変更する必要はなくなる。
#     print(service.greet(999))

# if __name__ == "__main__":
#     main()

#------------

# # 例3 使えないmain.py (FakeUserRepoを使う場合)
# from businesses.business import UserService
# from impls.broken import BrokenUserRepo

# def main() -> None:
#     service = UserService(BrokenUserRepo()) # ← これは失敗する(business.pyでは、AbstractUserRepoに従うimplを期待しているのに、brokenは従っていないから。)
#     print(service.greet(999))

# if __name__ == "__main__":
#     main()