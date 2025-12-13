// import { Component, signal } from '@angular/core';
// import { RouterOutlet } from '@angular/router';

// @Component({
//   selector: 'app-root',
//   imports: [RouterOutlet],
//   templateUrl: './app.html',
//   styleUrl: './app.css'
// })
// export class App {
//   protected readonly title = signal('project_angular_01');
// }


import {Component} from '@angular/core';
//ルーティングを有効化するためインポート
import {RouterOutlet} from '@angular/router';

@Component({
  selector: 'app-root',
  // router-outletをtemplateで使い、navタグで簡単なナビゲーションを追加
  template: `
    <h1>Welcome to Angular!</h1>
    <nav>
      <a href="/">Home</a>
      |
      <a href="/user">User</a>
    </nav>
    <router-outlet />
  `,
  //ルーティングを有効化するため↑でインポートしたRouterOutletをimportsに追加
  //これで、template内で<router-outlet>が使えるようになる
  imports: [RouterOutlet],
})
export class App {}

