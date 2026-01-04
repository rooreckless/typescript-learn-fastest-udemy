import { Injectable} from '@angular/core';
import { HttpClient } from '@angular/common/http';

@Injectable({ providedIn: 'root' })
export class UserService {
    // private readonly API = 'http://localhost/api';
    // https化に伴い、https://localhost/api に変更してもうまくいくことは確認したが、
    // 実際の運用では、nginxなどのリバースプロキシ経由や、dockercomposeネットワークでアクセスすることになるので、相対パスに変更した。
    private readonly API = '/api';
    constructor(private http: HttpClient) { // HttpClientをコンストラクタで注入
    }
    // private http = inject(HttpClient);
    getUsers() {
        return this.http.get(`${this.API}/users`);
        // return this.http.get('http://localhost/api/users', {responseType: 'json'});
    }

    createUser(data: any) {
        return this.http.post(`${this.API}/users`, data);
    }
}
