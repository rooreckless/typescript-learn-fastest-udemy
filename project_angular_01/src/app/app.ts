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

@Component({
  selector: 'app-user',
  template: `
    Username: {{ username }}
  `,
  styles: `
    :host {
      color: red;
    }
  `,
})
export class User {
  username = 'youngTech';
}

// ---コンポーネントの1つめapp-user↑と2つめapp-root↓---

@Component({
  selector: 'app-root',
  // app-rootセレクタのテンプレートは必ず描画される
  // ↑のapp-userセレクタのテンプレートも描画されるようにしてみる
  template: `
    abc<br>
    <section class="user-section">
      <app-user></app-user>
    </section>
    
  `,
  // export されているUserコンポーネントをここでimportして使う
  // そのうえでapp-userセレクタをテンプレートに記述する
  imports: [User],
  styles: `
    .user-section {
      border: 4px dashed blue;
    }
  `,
})
export class App {}
