/**
 * =========================================
 * メインアプリケーションコンポーネント
 * =========================================
 */

import { Component, OnInit, inject } from '@angular/core';
import { CommonModule } from '@angular/common';
import { RouterOutlet } from '@angular/router';
import { HttpClient } from '@angular/common/http';

/**
 * ユーザーインターフェース
 */
interface User {
  id?: number;
  username: string;
  email: string;
  created_at?: string;
}

@Component({
  selector: 'app-root',
  standalone: true,
  imports: [CommonModule, RouterOutlet],
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent implements OnInit {
  title = 'TAFP Application';
  users: User[] = [];
  apiStatus = 'checking...';
  private apiUrl = 'http://localhost:8000';
  private readonly http: HttpClient = inject(HttpClient);

  /**
   * コンポーネント初期化時の処理
   * APIからユーザーデータを取得
   */
  ngOnInit(): void {
    this.checkApiHealth();
    this.loadUsers();
  }

  /**
   * APIヘルスチェック
   */
  checkApiHealth(): void {
    this.http.get(`${this.apiUrl}/health`).subscribe({
      next: (response: unknown) => {
        this.apiStatus = '✅ Connected';
        console.log('API Health:', response);
      },
      error: (error: unknown) => {
        this.apiStatus = '❌ Disconnected';
        console.error('API Health Check Failed:', error);
      }
    });
  }

  /**
   * ユーザー一覧の読み込み
   */
  loadUsers(): void {
    this.http.get<User[]>(`${this.apiUrl}/api/users`).subscribe({
      next: (data: User[]) => {
        this.users = data;
        console.log('Users loaded:', data);
      },
      error: (error: unknown) => {
        console.error('Failed to load users:', error);
      }
    });
  }
}
