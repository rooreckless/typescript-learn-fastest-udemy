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


//-------------------------------------
// -- 抽象クラス abstract--
console.log("---抽象クラス--abstract----------------");

// 抽象クラスは、他のクラスが継承するための基底クラスとして設計されるクラス
// 抽象クラス自体はインスタンス化できない。
// 抽象クラスはabstractキーワードを使って定義される。

// 抽象クラスは、共通のプロパティやメソッドを持ち、
// さらに抽象メソッド(abstract method)を定義することができる。
// 抽象メソッドは、派生クラスで必ず実装しなければならないメソッドであり、
// 抽象クラス内では実装されない。
abstract class EmailSender{
    // コンストラクタ(ワンライナー形式)
    constructor(protected from: string){

    }
    // 抽象メソッドの定義
    abstract send(to: string, subject: string, body: string): boolean;
    // 抽象クラスで、通常のメソッドの定義は可能
    validateEmail(email: string): boolean{
        return email.includes("@");
    }
}

// 抽象クラスEmailSenderを継承したDevEmailSenderクラス
class DevEmailSender extends EmailSender{
    constructor(from: string){
        super(from);
    }
    // sendメソッドの実装は必須(抽象クラスEmailSenderでabstractとして定義されているため)
    send(to: string, subject: string, body: string): boolean{
        if (!this.validateEmail(to)){
            console.log("無効なメールアドレスです:", to);
            return false;
        }
        console.log(`[DevEmailSender] メール送信シミュレーション From: ${this.from}, To: ${to}, Subject: ${subject}, Body: ${body}`);
        return true;
    }
}

const dev_mailer = new DevEmailSender("system@example.com");
dev_mailer.send("test@example.com", "おしらせ", "テストメールです");


//------------------------------------
// 抽象クラスとinterfaceの違い
// 抽象クラスは共通のプロパティやメソッドの実装を提供できるが、interfaceは型の設計図を提供するだけで、実装は持たない。
// クラスは、1つの抽象クラスしか継承できないが、複数のinterfaceをimplementsできる。
// 抽象クラスは状態(プロパティ)を持てるが、interfaceは状態を持てない。
// 抽象クラスは継承関係を示すのに対し、interfaceは実装関係を示す。

// まとめると、抽象クラスは共通の実装を提供したい場合に使い、interfaceは異なるクラス間で共通の設計図を提供したい場合に使う。