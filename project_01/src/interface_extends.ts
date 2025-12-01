// インターフェースの拡張 interfaceとextends
console.log("---インターフェースの拡張 interfaceとextends----------------");

interface User{
    id: number;
    name: string;

}

interface AdminUser extends User{ // <- Userインターフェースを拡張してAdminUserインターフェースを定義
    role: "super" | "sub"; // <- 追加プロパティroleを定義
}



const admin1: AdminUser = {
    id: 1,
    name: "Alice",
    role: "super"
}

const subuser1: AdminUser = {
    id: 2,
    name: "Bob",
    role: "sub"
}

console.log("admin1=",admin1);
console.log("subuser1=",subuser1);


interface ContactInfo{ // <- 連絡先情報を表すインターフェース
    phone: string;
    address: string;
}

interface PremiumUser extends User, ContactInfo{ // <- 複数のインターフェースを拡張可能
    joinDate: string;
}

const premiumUser1: PremiumUser = {
    id: 3,
    name: "Charlie",
    phone: "123-456-7890",
    address: "123 Main St",
    joinDate: "2024-01-15"
}


console.log("premiumUser1=",premiumUser1);