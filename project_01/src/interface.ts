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