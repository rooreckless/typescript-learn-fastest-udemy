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
import {Comments} from './comments';

@Component({
  selector: 'app-root',
  // 親コンポーネントのtemplate内で子コンポーネントを使うが、
  // それのロードを遅延させるため@deferでラップする
  template: `
    <div>
      <h1>How I feel about Angular</h1>
      <article></article>
      @defer {
        <comments />
      }
    </div>
  `,
  // 子コンポーネントcommentsを使うためにimportsに追加
  imports: [Comments],
})
export class App {}

