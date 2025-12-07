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
  selector: 'app-root',
  // templateで、プロパティを表示させることができる
  template: `
    Hello {{ city }}
  `,
  // styleを変えると、localhost:4200にアクセスしたときの文字色が変わる
  styles: `
    :host {
      color: #a144db;
    }
  `,
})
export class App {
  // cityプロパティをコンポーネントクラスに追加(string型に型定義)
  city: string = 'San Francisco';
}
