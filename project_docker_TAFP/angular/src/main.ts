/**
 * =========================================
 * Angularアプリケーションのメインエントリーポイント
 * =========================================
 */

import { bootstrapApplication } from '@angular/platform-browser';
import { App } from './app/app.component';
import { appConfig } from './app/app.config';

/**
 * アプリケーションのブートストラップ
 * スタンドアロンコンポーネントを使用した最新のAngular構成
 */
bootstrapApplication(App, appConfig)
  .catch((err: unknown) => console.error(err));
