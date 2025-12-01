// interfaceとimplements

console.log("---interfaceとimplements------------------");

// interfaceはオブジェクトの型を定義するために使われる

interface UserInterface {
    name: string;
    age: number;
    
    // メソッドの定義も可能
    greet(): string;
}

interface Saveable{
    save(): void;
}

// interfaceを使ってクラスの設計図を定義し、その設計図に従ってクラスを実装するには、implementsキーワードを使う
class User_with_implements implements UserInterface,Saveable {
    //implementsを使ったので、そのインターフェースに定義されたプロパティとメソッドを
    // すべて実装する必要がある。ぬけているとコンパイルエラーになる。
    constructor(public name: string, public age: number){
        this.name = name;
        this.age = age;
    }

    greet(): string{
        return `こんにちは,${this.name}さん。`;
    }
    save(): void {
        console.log(`${this.name}さんのデータを保存しました。`);
    }
}

const user_with_implements = new User_with_implements("Alice", 28);
console.log(user_with_implements);
console.log(user_with_implements.greet());
user_with_implements.save();

// 以前、interfaceでオブジェクトの型定義をし、オブジェクトの作成の際はimplementsは使わなかったが、
// クラスで設計図を定義し、その設計図に従ってクラスを実装する場合にはimplementsを使うことが多い。

// --implementsを使う場面--

// 1. 開発環境と本番環境で「動作の詳細は変えたい」が、「機能自体は同じもの実装されていないといけない」場合
// 例1-1: メール送信機能 : 開発環境ではコンソールにログを出すだけ、本番環境では実際にメールを送信するクラスを実装する。
// ただ、どちらの環境だとしても「メールを送信する機能」自体は存在するべきなので、interfaceで設計図を定義し、両方のクラスでimplementsを使ってその設計図に従わせる。

// 例1-2: データ保存機能 : 開発環境ではローカルストレージに保存、本番環境ではサーバーに保存するクラスを実装する。

// 2. 複数のクラスで共通の機能を持たせたいが、継承関係にはしたくない場合
// 3. 大規模開発で、設計段階でクラスの設計図を明確にしておきたい場合