import { ApplicationConfig, provideZoneChangeDetection,inject } from '@angular/core';
import { provideRouter } from '@angular/router';
import { routes } from './app.routes';

import { provideHttpClient, withInterceptors } from '@angular/common/http';
import { AuthService } from './services/auth';

// HTTPインターセプターの定義(exportしておらず、このファイル内でのみ使用)
const authInterceptor = (req: any, next: any) => {
  const auth = inject(AuthService);
  const token = auth.getToken();

  if (!token) {
    return next(req);
  }

  const authReq = req.clone({
    setHeaders: {
      Authorization: `Bearer ${token}`,
    },
  });

  return next(authReq);
};

export const appConfig: ApplicationConfig = {
  providers: [
    provideZoneChangeDetection({ eventCoalescing: true }),
    provideRouter(routes),  // app.routesで作成したルーティングを提供できるようにする=provideRouter(routes)
    // HttpClientを提供し、authInterceptorをHTTPリクエストに適用
    provideHttpClient(
      withInterceptors([authInterceptor])
    ),
  ]
};