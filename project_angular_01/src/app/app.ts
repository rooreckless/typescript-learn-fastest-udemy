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
import {User} from './user';

// ルートコンポーネントではuserコンポーネントを使用するがそれだけ
@Component({
  selector: 'app-root',
  // Userコンポーネントにnameプロパティを渡す
  template: `
    <app-user name="Simran"/>
  `,
  imports: [User],
})
export class App {}
