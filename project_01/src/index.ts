// 型注釈(型アノテーション)の基本
console.log("---型注釈(型アノテーション)の基本------------------");
let userName: string ="太郎";
let age: number = 30;
let isStudent: boolean = true;

console.log("userName=", userName);
console.log("age=", age);
console.log("isStudent=", isStudent);

console.log("---型推論とは------------------");
// 型推論
let userName2 = "花子"; // string型と推論される
let age2 = 25;
let isStudent2 = false;

console.log("userName2=", userName2);
console.log("age2=", age2);
console.log("isStudent2=", isStudent2);

//---------------------------------------
// 型推論と明示的な型注釈の使い分け
// 1. 型推論で十分な場合 = 変数名で、値の型が明確な場合
// 2. 型推論で十分な場合 = 変数定義時に初期値を設定する場合

// 1. 明示的な型注釈を書くべき場合 = 関数の引数と戻り値(関数のインターフェースを明確にした方が使いやすい)
// 2. 明示的な型注釈を書くべき場合 = 変数を宣言したときには初期化をしないとき
// 3. 明示的な型注釈を書くべき場合 = 複雑な型を扱ったりして、型推論にまかせたらAny型にしかならない場合
//---------------------------------------

//---------------------------------------
// --関数の型注釈 = 引数と戻り値に型注釈をつけること--
console.log("---関数の型注釈 = 引数と戻り値に型注釈をつけること------------------");
function add1(a: number, b: number): number {
    return a + b;
}
// その関数を使うときにエラーになる例
const result1 = add1(10, 20);
console.log(result1);
// const result2 = add1("10", "20"); // <- エラー

// アロー関数に型注釈する場合
console.log("---アロー関数に型注釈 = 引数と戻り値に型注釈をつけることは一緒------------------");
const add2 = (a: number, b: number): number => {
    return a + b;
};

// その関数を使うときの例
const result2 = add2(15, 25);
console.log(result2);
// その関数を使うときにエラーになる例
// const result3 = add2("15", "25"); // <- エラー


//---------------------------------------
// --NaNとInfinityの扱いと型注釈の限界と対処方法--
console.log("---NaN(Not a Number)の例------------------");

// NaN(Not a Number = 数字として扱えないものになってしまっている状態)の例

let resultNaN1 :number = 0/0;
console.log(resultNaN1); // <- NaN
// console.log(resultNaN1 === NaN); // <- trueにならず常にFalseのエラーになる NaNはNaN同士で比較できないisNaNが必要
console.log(Number.isNaN(resultNaN1)); // <- true

let resultNaN2 :number = parseInt("こんにちは");
console.log(resultNaN2); // <-  NaN

console.log("---Infinity(無限大の例)------------------");

// Infinity(無限大の例)
let resultInf1 :number = 1/0;
console.log(resultInf1); // <- Infinity

console.log(resultInf1 === Infinity); // <- true
console.log(Number.isFinite(resultInf1)); // <- false = Infinityであるということ

let resultInf2 :number = -1/0;
console.log(resultInf2); // <- -Infinity
console.log(Number.isFinite(resultInf2)); // <- false = -InfinityでもInfinityであるということ

// なぜNaNとInfinityのチェック関数までまなんだのか
// -> 型注釈だけでは、Number型であることは指定できても、計算した結果、NaNやInfinityになることまでは型注釈で防げないから
//   -> なので、計算結果がNaNやInfinityになっていないかをチェックする関数が必要になる

//---------------------------------------
console.log("---配列の型注釈 1. []を使う方法------------------");
// -- 配列の型注釈 1. []を使う方法

let names: string[] = ["太郎", "花子", "次郎"];
let ages: number[] = [20, 25, 30];
let flags: boolean[] = [true, false, true];

// 配列の中身を確認する例
console.log(names);
console.log(typeof names); // typeof演算子は配列に対しては"object"を返すので、これだけだと配列かどうかわからない
console.log(Array.isArray(names)); // <- 配列かどうかを判定するにはArray.isArray()を使う
names.forEach(elem => {
    console.log("names elem type=" + typeof elem); // <- 配列の各要素の型はstringであることがわかる
});

console.log(ages);
console.log(Array.isArray(ages)); // <- 配列かどうかを判定するにはArray.isArray()を使う
for (const elem of ages){
    console.log("ages elem type=" + typeof elem); // <- 配列の各要素の型はnumberであることがわかる
}
console.log(typeof ages);
console.log(flags);
console.log(typeof flags);
for (let i = 0; i < flags.length; i++){
    console.log("flags elem type=" + typeof flags[i]); // <- 配列の各要素の型はbooleanであることがわかる
}

console.log("---配列の型注釈 2. ジェネリクスを使う方法------------------");

// -- 配列の型注釈 2. ジェネリクスを使う方法

let names2: Array<string> = ["一郎", "二郎", "三郎"]; // そもそもジェネリクスとは<>で囲まれた部分のこと
let ages2: Array<number> = [22, 28, 35];
let flags2: Array<boolean> = [false, true, false];

console.log(names2);
console.log(typeof names2);
console.log(ages2);
console.log(typeof ages2);
console.log(flags2);
console.log(typeof flags2);

//---------------------------------------
// -- オブジェクトの型注釈 --
console.log("---オブジェクトの型注釈------------------");
// jsでのオブジェクトは以下のような形でした

// let userJS = {name: "太郎", age: 30};

// tsでのオブジェクトの型注釈は以下のように書きます
// プロパティnameはstring型、ageはnumber型であることを指定
let user: {name: string, age: number} = {
    name: "太郎",
    age:30
};

console.log("user=",user);

// オブジェクトのネストも可能
// user2オブジェクトの「addressプロパティがオブジェクト」である例
let user2: { 
    name: string, age: number,
    address: {city: string, zipCode:string}
} = {
    name: "太郎",
    age:30,
    address: {city: "東京", zipCode: "000-0000"}
};

console.log("user2=",user2);


//---------------------------------------
// Any型

console.log("---Any型------------------");

let value: any = "test";
console.log("value=", value);
value = 123;
console.log("value=", value);
value = true;
console.log("value=", value);
value= {};
console.log("value=", value);

// ↑エラーにならない。つまり、any型なvalueには、どんな型の値でも代入できる。

// any型の危険性の例
let userAny: any  = {name: "太郎", age: 30};
console.log("userAny=", userAny);
console.log("userAny=", userAny.aaaaaa);
// ↑ userAnyはany型なので、存在しないプロパティaaaaaaにアクセスしてもエラーにならず、undefinedになっている。
// console.log("userAny=", userAny.aaaaaa.toUpperCase());
// ↑ もっと危険なのが↑ 上記のようにundefinedに対してさらにメソッドを呼び出そうとすると、ランタイムエラーになる。
// ランタイムエラー = 実行時エラーなので、「tscでのコンパイル時には気付けない」ことになる。userAnyがany型だから

// Any型を使う状況
// 1. 型がわからない外部ライブラリを使うとき
// 2. とりあえず型注釈を後回しにしたいとき(開発初期段階や、JsからTsへの移行を段階的に行う場合)
// 3. それ以外は基本的にany型は使わないことを推奨



// ---------------------------------------
// 型ガード　= コンパイル時ではなく、実行時に型をチェックして、Tsに正しい型を認識させる仕組み。
console.log("---型ガード------------------");
// typeof演算子を使った型ガードの例
function process(value: any){
    if (typeof value === "string"){
        return value.toUpperCase(); // toUpperCaseは「valueがstring型でないと使えない」ので、typeofで型を保証させた。
    }else if (typeof value === "number"){
        return value.toString(2); // toString は「valueがnumber型でないと使えない」ので、typeofで型を保証させた。
    }else if (typeof value === "boolean"){
        return value ? "true" : "false"; // 三項演算子もboolean型でないと使えないので、typeofで型を保証させた。
    }else if (value instanceof Error){
        // まずvalueがオブジェクトの場合、「instanceof演算子で何オブジェクトか」を特定するのがいい。今回はErrorオブジェクトの場合ということ。
        return value.message; // Errorオブジェクトのmessageプロパティにアクセスするために、instanceofで型を保証させた。
    }else {
        return "処理できない型です";
    }
}

console.log(process("hello")); // <- "HELLO"
console.log(process(10)); // <- "1010"
console.log(process(true)); // <- "true"
console.log(process(new Error("何か問題が発生しました"))); // <- "何か問題が発生しました"
console.log(process({})); // <- "処理できない型です"

// ---------------------------------------
// 【余談】自分でclassを定義したうえで作成したオブジェクトとinstanceof
console.log("---【余談】instanceofの基本的な使い方------------------");
// 参考は https://ja.javascript.info/instanceof
class Rabbit {
    legs: number;
    speed: number;
    constructor(legs: number, speed: number){
        this.legs = legs;
        this.speed = speed;
    }
}

let rabbit = new Rabbit(4, 50);

console.log(rabbit instanceof Rabbit); // <- true
console.log(rabbit instanceof String); // <- false
console.log(rabbit instanceof Object); // <- true
console.log(rabbit instanceof Error); // <- false