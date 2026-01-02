import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';

@Injectable({
  providedIn: 'root',
})
export class AuthService {
  private readonly API = 'http://localhost/api';

  constructor(private http: HttpClient) {}

  // ログインメソッド
  login(email: string, password: string) {
    return this.http.post<any>(`${this.API}/auth/login`, {
      email,
      password,
    });
  }
  // JWTトークンをローカルストレージに保存するメソッド
  saveToken(token: string) {
    localStorage.setItem('access_token', token);
  }
  
  // ローカルストレージからトークンを取得するメソッド
  getToken(): string | null {
    return localStorage.getItem('access_token');
  }
  // ログアウトメソッド = ローカルストレージからトークンを削除する
  logout() {
    localStorage.removeItem('access_token');
  }
}
