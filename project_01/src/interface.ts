// インターフェース = データの仕様を定義するためのもの


// --オブジェクトの仕様を定義するインターフェース--
console.log("---オブジェクトの仕様を定義するインターフェース------------------");
interface User {
    // 「Userオブジェクトはnameとageプロパティを持つ必要がある」ことを定義
    name: string;
    age: number;

}

// Userインターフェースを使って実装したオブジェクト
const user1: User = {
    // Userインターフェースに従ってプロパティを定義=nameとageが必要で、値の型も一致が必要
    name: "Alice",
    age: 30,
    // email: "alice@example.com" // <- インターフェースに定義されていないプロパティはエラーになります
}

console.log(user1);


// --関数の仕様を定義する「関数インターフェース」 = call signature--
console.log("---関数の仕様を定義するインターフェース------------------");

// 関数のインターフェースとは「関数の引数と戻り値の型を」定義する
interface Calculator {
    // このインターフェースで実装する関数は、「2つのnumber型の引数を受け取り、number型の値を返す必要がある」
    (x: number, y:number): number;
}

// 関数インターフェースCalculatorを使って実装した関数addとmultiply
const add: Calculator = (x,y) => {
    return x+y;
}

console.log(add(5,3)); // 8

const multiply: Calculator = (x,y) => {
    return x*y;
}

console.log(multiply(5,3)); // 15

//-------------------------------------------------

// --関数インターフェースの応用例 callback関数--
console.log("---関数インターフェースの応用例------------------");

interface EventHandler{
    (message: string): void;
}

function Process(input: string, handler: EventHandler): void{
    // この関数は、文字列inputを受け取り、処理が完了したらhandlerコールバック関数を呼び出す
    // handlerがどんな関数かは使われるとき次第だが、少なくともEventHandlerインターフェースに従う必要がある
    handler(`処理完了: ${input}`);
}

const logger: EventHandler = (message) => {
    // ↑のProcess関数に渡すコールバック関数
    console.log(message);
}


// ↓1.まず Process関数を呼び出し、loggerコールバック関数を渡す
// ↓2. Processの中ではhandlerを実行 = loggerが実行されるということ
// ↓3. そのloggerの引数messageの内容は`処理完了: ${input}`だが、そのinputは"てすとでーた"である
Process("てすとでーた", logger); // <- コンソールに「処理完了: てすとでーた」と表示される  
// ↑の流れの中でProcessがhandler引数の関数を実行する際、
// 「事前に関数インターフェースを作成し、それに従った関数を渡す」ようにしないと実行できない。(handlerにあらゆる型の引数を渡していいことにはできないから。)
// だから、loggerはEventHandlerインターフェースに従わせた。


//-------------------------------------------------
// -- オプショナルプロパティとインターフェース--
console.log("---オプショナルプロパティとインターフェース------------------");

interface User_Optional {
    // オブジェクトインターフェース
    name: string;
    age?: number; // <- ageプロパティはオプショナル(あってもなくても良い)
    email?: string; // <- emailプロパティもオプショナル(あってもなくても良い)
}

const user_optional1: User_Optional= {
    name: "Bob",
    // ageとemailはオプショナルなので、省略可能
}
console.log(user_optional1);
console.log(user_optional1.email); // <- 存在しない可能性があるのでundefinedになる可能性がある

const user_optional2: User_Optional= {
    name: "Charlie",
    age: 25,
    // ageとemailはオプショナルなので、省略可能
}

console.log(user_optional2);

// --オプショナルプロパティなインターフェースを使う場合---
// オプショナルプロパティは存在しない可能性があるので、アクセスする際には型ガードなどで存在チェックを行うのが一般的
// オプショナルプロパティを使う状況
// 1. ユーザー情報の一部が未提供の場合
// 2. APIからのレスポンスで一部のデータが欠落している場合
// 3. フォームの情報で一部が未入力でも許容されるケース 

// 関数インターフェースでもオプショナルプロパティ(というかオプショナル引数)を使ってみる
console.log("---関数インターフェースでオプショナル引数------------------");
interface Logger {
    (message: string, level?: string): void; // level引数はオプショナル
}

const simpleLogger: Logger = (message, level) => {
    if(level){
        console.log(`[${level}] ${message}`);
    } else {
        console.log(message);
    }
}

simpleLogger("システムが起動しました"); // level引数を省略した場合
simpleLogger("ユーザーがログインしました", "INFO"); // level引数を指定した場合

//-------------------------------------------------
// --インターフェースで使えるリードオンリーキーワード--
console.log("---インターフェースで使えるリードオンリーキーワード------------------");

interface User_Readonly{
    readonly id: number; // <- idプロパティは読み取り専用(readonly)
    name: string;
}

const user_readonly1: User_Readonly = {
    id: 1,
    name: "David"
}

user_readonly1.name = "Daniel"; // nameプロパティは変更可能
console.log(user_readonly1);

// user_readonly1.id = 2; // <- コンパイルエラー: 'id'は読み取り専用プロパティです

// 【念の為】constとreadonlyの違い
// constは変数自体の再代入を禁止するキーワード
// なので、constで宣言したオブジェクトでも、そのプロパティの変更は可能(↑のnameプロパティのように)
// もちろん、const自体は再代入禁止だから、user_readonly1 = { id: 2, name: "Eve" } // <- これは再代入なのでエラーになる
// 一方、readonlyはオブジェクトのプロパティの変更を禁止するキーワード
