// 型注釈(型アノテーション)の基本
let userName: string ="太郎";
let age: number = 30;
let isStudent: boolean = true;

// 型推論
let userName2 = "花子"; // string型と推論される
let age2 = 25;
let isStudent2 = false;

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

function add1(a: number, b: number): number {
    return a + b;
}
// その関数を使うときにエラーになる例
const result1 = add1(10, 20);
console.log(result1);
// const result2 = add1("10", "20"); // <- エラー

// アロー関数に型注釈する場合
const add2 = (a: number, b: number): number => {
    return a + b;
};

// その関数を使うときの例
const result2 = add2(15, 25);
console.log(result2);
// その関数を使うときにエラーになる例
// const result3 = add2("15", "25"); // <- エラー


//---------------------------------------
// --NaNとInifityの扱いと型注釈の限界と対処方法--
console.log("---------------------")

// NaN(Not a Number = 数字として扱えないものになってしまっている状態)の例

let resultNaN1 :number = 0/0;
console.log(resultNaN1); // <- NaN
// console.log(resultNaN1 === NaN); // <- trueにならず常にFalseのエラーになる NaNはNaN同士で比較できないisNaNが必要
console.log(Number.isNaN(resultNaN1)); // <- true

let resultNaN2 :number = parseInt("こんにちは");
console.log(resultNaN2); // <-  NaN


// Infinitity(無限大の例)
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