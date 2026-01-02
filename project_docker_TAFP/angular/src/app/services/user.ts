import { Injectable} from '@angular/core';
import { HttpClient } from '@angular/common/http';

@Injectable({ providedIn: 'root' })
export class UserService {
    constructor(private http: HttpClient) { // HttpClientをコンストラクタで注入
    }
    // private http = inject(HttpClient);
    getUsers() {
    return this.http.get('http://localhost/api/users');
        // return this.http.get('http://localhost/api/users', {responseType: 'json'});
    }
}
