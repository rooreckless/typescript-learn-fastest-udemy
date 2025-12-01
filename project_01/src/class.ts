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

//------------------------------------

// -- アクセス修飾子 typescript独自の仕組み public private protected---
console.log("---アクセス修飾子---public---------------");

class User_withAccessModifiers_public{
    public name: string; // publicはデフォルトなので、省略可能
    public age: number;
    
    constructor(name: string, age: number){
        this.name = name;
        this.age = age;
    }

    public greet(): string{
        return `こんにちは,${this.name}さん。`;
    }
}

const user_withPublic = new User_withAccessModifiers_public("Taro", 40);
console.log(user_withPublic.name); // publicなので「クラスの外から」アクセス可能
user_withPublic.age = 41; // ageはpublicなので「クラスの外から」アクセス可能で変更可能
console.log(user_withPublic.age); // 41 <- もともと40だったのに41に変更できている
console.log(user_withPublic.greet()); // publicなので「クラスの外から」アクセス可能


console.log("---アクセス修飾子---private---------------");


class User_withAccessModifiers_private{
    public name: string; // publicなので「クラスの外から」アクセス可能
    private age: number; // privateは「クラスの外から」アクセス不可
    
    constructor(name: string, age: number){
        this.name = name;
        this.age = age;
    }

    // ちなみに、constractorの引数自体にアクセス修飾子をつけると、自動的にプロパティとして定義されるので、上記のように別途プロパティ定義を書く必要はなくなる
    // 例:
    // constructor(public name: string, private age: number){
    //     // this.name と this.age は自動的に定義される
    // }

    public greet(): string{
        return `こんにちは,${this.name}さん。`;
    }

    public getAge(): number{
        // privateなageプロパティに「クラスの内側から」アクセスして値を返す
        // つまり、このgetAgeメソッド自体には「クラスの外側からアクセス」可能なので。
        return this.age;
    }
}

const user_withPrivate = new User_withAccessModifiers_private("Hanako", 45);
console.log(user_withPrivate.name); // publicなので「クラスの外から」アクセス可能
// console.log(user_withPrivate.age); // コンパイルエラー: privateなので「クラスの外から」アクセス不可
console.log(user_withPrivate.getAge()); // 45 <- getAgeメソッド経由ならageプロパティの値を取得できる

//-------------------------------------

console.log("---アクセス修飾子---protected---------------");

class User_withAccessModifiers_protected{
    protected name: string; // protectedなので「クラスの内側から,または、継承したクラスの内部からなら」アクセス可能
    private age: number; // privateは「クラスの外から」アクセス不可
    
    constructor(name: string, age: number){
        this.name = name;
        this.age = age;
    }

    public greet(): string{
        return `こんにちは,${this.name}さん。`;
    }

    public getAge(): number{
        return this.age;
    }
    public getName(): string{
        return this.name;
    }
}

const user_withProtected = new User_withAccessModifiers_protected("Kenta", 50);
// console.log(user_withProtected.name); // コンパイルエラー: protectedなので「クラスの外から」アクセス不可
console.log(user_withProtected.getName()); // Kenta <- getNameメソッド経由ならnameプロパティの値を取得できる

// 「protetedなプロパティを含むクラス」を継承したクラスを作成
class AdminUser_withAccessModifiers_protected extends User_withAccessModifiers_protected{
    private role: string;

    constructor(name: string, age: number, role: string){
        super(name, age);
        this.role = role;
    }

    public displayAdminInfo(): string{
        return `管理者: ${this.name}, 年齢: ${this.getAge()}, 役割: ${this.role}`;
        // ↑ここで、protectedなnameプロパティに${this.name}で、「継承したクラスの内側から」アクセスしている
        // 一方、ageプロパティはprivateなので、this.ageではアクセスできないため、getAge()メソッド経由で値を取得している
    }
}

const adminUser_withProtected = new AdminUser_withAccessModifiers_protected("Mika", 55, "SuperAdmin");
// console.log(adminUser_withProtected.name); // コンパイルエラー: protectedなので「クラスの外から」アクセス不可
console.log(adminUser_withProtected.displayAdminInfo()); // 管理者: Mika, 年齢: 55, 役割: SuperAdmin

