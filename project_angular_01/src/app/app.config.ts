import { ApplicationConfig, provideBrowserGlobalErrorListeners } from '@angular/core';
import { provideRouter } from '@angular/router';

import { routes } from './app.routes';

// appConfigをエクスポートしている。
// ApplicationConfig型で型付けされたオブジェクトである。
// そのプロパティはprovidersで配列を持ち、
// app.routes.tsで定義されたルート情報を使ってルーターを提供するためのprovideRouter関数と、
// ブラウザのグローバルエラーリスナーを提供するためのprovideBrowserGlobalErrorListeners関数を呼び出している。
// つまり、app.routes.tsで、ルーティング情報を記載することになる。
export const appConfig: ApplicationConfig = {
  providers: [
    provideBrowserGlobalErrorListeners(),
    provideRouter(routes)
  ]
};
