// intersection型

// 交差 重複の意味

// intersection 「AかつB」(=「AとBの両方」)の意味　←→　union型 AまたはBの意味

// intersection型に使える組み合わせは、「型エイリアス(type)同士」、「interface同士」、「型エイリアスとinterfaceの組わせ」のどれでもok

// 実際的な使い方は、「オブジェクト型同士」での使い方がされやすい

console.log("---intersection型------------------");

type PersonalInfoType = {
    name: string;
    age: number;
}

type ContactInfoType = {
    email: string;
}

// ↓intersection型で型エイリアス同士(PersonalInfoTypeとContactInfoType)を組み合わせてUserProfileIntersection1型を定義
// つまりインターセクションでまとめられた全インターフェスのプロパティ、name, age, emailプロパティすべてを持っている
type UserProfileIntersection1 = PersonalInfoType & ContactInfoType; 


const user1: UserProfileIntersection1 = {
    // ↑UserProfileIntersection1型オブジェクトを作るには、インターセクションでまとめられた全インターフェスのプロパティ
    // name, age, emailプロパティのすべてを必要とする
    name: "Daisuke",
    age: 30,
    email: "daisuke@example.com"
}

console.log("user1=",user1);


interface PersonalInfoInterface{
    name: string;
    age: number;
}

// ↓intersection型で「インターフェースと型エイリアス」(PersonalInfoInterfaceとContactInfoType)を組み合わせてUserProfileIntersection2型を定義
type UserProfileIntersection2 = PersonalInfoInterface & ContactInfoType; 

const user2: UserProfileIntersection2 = {
    name: "Emiko",
    age: 30,
    email: "emiko@example.com"
}

console.log("user2=",user2);

