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
//  【追加】さらに、RouteLinkもインポート
import {RouterOutlet,RouterLink} from '@angular/router';

@Component({
  selector: 'app-root',
  // router-outletをtemplateで使い、navタグで簡単なナビゲーションを追加
  //  【追加】さらに、RouterLinkディレクティブを使ってリンクを設定し、aタグのhref属性をrouterLink属性に変更
  template: `
    <h1>Welcome to Angular!</h1>
    <nav>
      <a routerLink="/">Home routeLink</a>
      |
      <a routerLink="/user">User routeLink</a>
    </nav>
    <router-outlet />
  `,
  //ルーティングを有効化するため↑でインポートしたRouterOutletをimportsに追加
  //これで、template内で<router-outlet>が使えるようになる
  // 【追加】さらにRouterLinkの追加インポートにも対応 
  imports: [RouterOutlet,RouterLink],
})
export class App {}

