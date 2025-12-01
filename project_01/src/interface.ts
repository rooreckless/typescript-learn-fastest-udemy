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

//-------------------------------------------------
// -- ネストしたインターフェース
console.log("---ネストしたインターフェース------------------");

interface Product { // <- 商品を表すインターフェース
    id: number;
    name: string;
    price: number;

}

interface OrderItem {  // <- 注文アイテムを表すインターフェース
    product: Product; // <- ネストしたインターフェース = productプロパティはProductインターフェースに従うオブジェクト
    quantity: number;
}

const orderItem1: OrderItem ={
    product: {
        id: 1,
        name: "ノートPC",
        price: 98000,
    },
    quantity: 2
}

console.log("orderItem1=",orderItem1);

// OrderItemインターフェースをさらにネスト、しかも配列にして使う例

interface Order{   // <- 注文を表すインターフェース
    id: number;
    customerName: string;
    items: OrderItem[]; // <- OrderItemインターフェースの配列
}

const order1: Order = {
    id: 1001,
    customerName: "Emma",
    items: [
        {product: {id: 1, name: "ノートPC", price: 98000}, quantity: 1},
        {product: {id: 2, name: "マウス", price: 2500}, quantity: 2}
    ],
}

console.log("order1=", order1);

// -------------------------------------------------
// -- 型エイリアス
console.log("---型エイリアス------------------");

// 型エイリアス = 型に別名をつける機能
type UserAlias = {
    id: number;
    name: string;
    email: string;

};

const user_alias1: UserAlias = {
    id: 1,
    name: "Frank",
    email: "frank@example.com"
};

console.log(user_alias1)

// 別の型エイリアス
type StatusAlias = "loading" | "success" | "error";
function checkStatus(status: StatusAlias): void {
    console.log(`現在のステータス: ${status}`);
}
checkStatus("loading");
checkStatus("success");
// checkStatus("complete"); // <- コンパイルエラー: 'complete'はStatusAlias型に含まれていない


//-------------------------------------------------
// -- 型エイリアスで、関数の型を定義する

console.log("---型エイリアスで関数の型を定義する------------------");

type CalculatorAlias = (x: number, y: number) => number;

const addAlias: CalculatorAlias = (x,y) => {
    return x + y;
};

console.log(addAlias(10,15)); // 25

// --型エイリアスでもcallback関数を定義してみる(以前インターフェースでやったことと同じようなことをしてみる)

type EventHandlerAlias = (message: string) => void;

function ProcessAlias(input: string, handler: EventHandlerAlias): void {
    handler(`処理完了: ${input}`);
}

const loggerAlias: EventHandlerAlias = (message) => {
    console.log(message);
};

ProcessAlias("テストデータ", loggerAlias); // <- コンソールに「処理完了: テストデータ」と表示される

// -------------------------------------------------
// -- 型エイリアスの有効な活用方法 = プリミティブ型に意味のある名前をつけること
console.log("---型エイリアスの有効な活用方法--プリミティブ型に意味のある名前をつけること----------------");

type UserID = number; // <- UserIDという型エイリアスをnumber型に対して定義

type User_useful_Alias = {
    // id: number; // <- これでも動作はするけど、ただのnumber型なので意味がわかりにくい。
    id: UserID; // <- UserID型を使ってidプロパティを定義
    name: string;
}

const user_useful_alias1: User_useful_Alias = {
    id: 1,
    name: "Grace"
};

const user_useful_alias2: User_useful_Alias = {
    id: 2,
    name: "Hank"
};

console.log(user_useful_alias1);
console.log(user_useful_alias2);

// ↑のように型エイリアスを使うことで、idプロパティがただのnumber型ではなく「UserIDであること」が明示され、コードの可読性と意味が向上する。

// ↓型エイリアスUser_useful_Aliasの配列型として定義し、内容はuser_useful_alias1とuser_useful_alias2を持つ配列
const users_useful_alias: User_useful_Alias[] = [user_useful_alias1, user_useful_alias2];

function getUserByUserId(id: UserID): User_useful_Alias | null {
    // 引数idはUserID型。(number型ではなくUserID型とすることで、意味がわかりやすい。)
    // これと一致するidプロパティを持つUser_useful_Aliasオブジェクトを配列から探して返す関数
    return users_useful_alias.find(user => user.id === id) || null;
}

console.log(getUserByUserId(1)); // <- user_useful_alias1オブジェクトを返す
console.log(getUserByUserId(3)); // <- nullを返す(存在しないidのため)

// -- 型エイリアスの有効な活用方法 = 複雑な型定義を整理するのに使える(入れ子を多用したり、ユニオン型を多用した型を整理するのに使う)
console.log("---型エイリアスの有効な活用方法--複雑な型定義を整理するのに使える----------------");

type Language = "JavaScript" | "TypeScript" | "Python" | "Java"; // <- リテラル型とユニオン型を組み合わせた型エイリアス(Enumみたいに。)
type AppId = number; // ↑で使った、「プリミティブ型(number)に意味のある名前をつける」例

type ProductApp = {
    readonly id: AppId;
    name: string;
    preferences:{ 
        language: Language; // <- preferencesプロパティはネストしたオブジェクトで、そのlanguageプロパティは型エイリアスLanguageに従う
                            // <- つまり、"JavaScript" | "TypeScript" | "Python" | "Java"のいずれかの文字列である必要がある
    }
}

const app1: ProductApp = {
    id: 101,
    name: "Code Editor",
    preferences: {
        language: "TypeScript"
    }
};

console.log(app1);

// ---インターフェースを使う場合と、型エイリアスを使う場合の違い---
// 基本的にはどちらを使っても良いが、以下のような違いがある
//
// インターフェース:
// - オブジェクトの型定義 : オブジェクトの形状を定義するのに最適 
// - 関数の型定義にも使える
// - (◯)extendsによる拡張 : 「継承」が可能で、元となるインターフェースを使い、他のインターフェースを拡張できる
// - 宣言のマージが可能(同じ名前のインターフェースを複数回宣言すると、それらが結合される)
//
//
// 型エイリアス:
// - (◯)プリミティブ型、ユニオン型、タプル型など、あらゆる型に名前を付けることができる
// - オブジェクトや関数の型定義にも使えるけど、interfaceほど直感的ではない場合もある
// - 複雑な型定義を整理するのに便利
// - extendsによる拡張はできない。しかし、Intersection Types(交差型)を使って似たような効果を得ることは可能
// - 宣言のマージはできない