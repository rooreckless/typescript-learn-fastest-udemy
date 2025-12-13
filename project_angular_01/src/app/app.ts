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
// 子コンポーネントuserをインポート
import {User} from './user';
@Component({
  selector: 'app-root',
  template: `
    <app-user></app-user>
  `,
  // 子コンポーネントUserを使うためにimportsに追加
  imports: [User],
})
export class App {}

