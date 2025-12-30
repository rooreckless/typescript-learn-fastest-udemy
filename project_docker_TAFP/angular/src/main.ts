/**
 * =========================================
 * Angularアプリケーションのメインエントリーポイント
 * =========================================
 */

import { bootstrapApplication } from '@angular/platform-browser';
import { App } from './app/app.component';
// import { provideRouter } from '@angular/router';
// import { provideHttpClient, withFetch } from '@angular/common/http';
// import { routes } from './app/app.routes';

/**
 * アプリケーションのブートストラップ
 * スタンドアロンコンポーネントを使用した最新のAngular構成
 */
bootstrapApplication(App, {
  providers: [
    // ルーティングの設定
    // provideRouter(routes),
    // HTTPクライアントの設定（Fetch APIを使用）
    // provideHttpClient(withFetch()),
  ]
}).catch((err: unknown) => console.error(err));
