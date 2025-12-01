// まず、Typescriptの前に、基本的なJavaScriptでのクラスの定義と継承の方法を確認しておきましょう。

// class User_in_BasicJS{
//     // コンストラクタ
//     constructor(name, age){
//         this.name=name;
//         this.age = age;
//     }
//     // メソッド
//     greet(){
//         return `こんにちは,私は${this.name}、${this.age}歳です。`;
//     }
// }

// // クラスの継承
// class AdminUser_in_BasicJS extends User_in_BasicJS{
//     constructor(name, age, role){
//         // 親クラスのコンストラクタを呼び出し
//         super(name, age);
//         // 親クラスには存在しない、子クラス独自のプロパティをコンストラクタに追加
//         this.role = role;
//     }
// }

// // インスタンスの生成とメソッドの呼び出し
// const user_in_BasicJS = new User_in_BasicJS("Taro", 25);
// console.log(user_in_BasicJS.greet()); // こんにちは,私はTaro、25歳です。

// const adminUser_in_BasicJS = new AdminUser_in_BasicJS("Hanako", 28, "Administrator");
// console.log(adminUser_in_BasicJS.greet()); // こんにちは,私はHanako、28歳です。
// console.log(`役割: ${adminUser_in_BasicJS.role}`); // 役割: Administrator

// // ↑は一応動くが、コンパイル的にはエラーになるので、全部コメントアウトしています。

// 次に、TypeScriptでのクラスの定義と継承の方法を確認しましょう。

console.log("---class------------------");

class User{
    // まずプロパティの定義と型注釈が必要(コンストラクタでthisだけじゃだめ)
    name: string;
    age: number;

    // コンストラクタ(引数の型注釈が必要)
    constructor(name: string, age: number){
        this.name = name;
        this.age = age;
    }
    // メソッド(戻り値の型注釈や、引数がつくならそれの型注釈が必要)
    greet(message: string): string{
        return `${message},${this.name}さん。`;
    }

    updateAge(newAge: number): void{
        this.age = newAge;
    }
}

// クラスの継承
class AdminUser extends User{
    role: string;

    constructor(name: string, age: number, role: string){
        // 親クラスのコンストラクタを呼び出し
        super(name, age);
        // 親クラスには存在しない、子クラス独自のプロパティをコンストラクタに追加
        this.role = role;
    }
}

// インスタンスの生成とメソッドの呼び出し
const user = new User("Taro", 35);
console.log(user.greet("こんにちは")); // こんにちは,Taroさん。
user.updateAge(36);
console.log("UPDATED user.age=", user.age); //UPDATED user.age= 36

const adminUser = new AdminUser("Hanako", 38, "Administrator");
console.log(adminUser.greet("こんにちは")); // こんにちは,Hanakoさん。
console.log(`役割: ${adminUser.role}`); // 役割: Administrator