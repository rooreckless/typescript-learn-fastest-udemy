//依存性逆転も試してみる。

// サービスを使う側(app.ts)のための、サービス側が守らなければならない実装ルールを定義する抽象クラス
export abstract class AbstractCartService {
  abstract getCars(): string[];
  abstract getCar(id: number): string;
}
