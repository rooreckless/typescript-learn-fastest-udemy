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
// パイプを使うためにimport
import { UpperCasePipe } from '@angular/common';

// テンプレートでパイプを使う例
@Component({
  selector: 'app-root',
  template: `
  username = {{ username}}<br>  
  username | uppercase = {{ username | uppercase }}
  `,
  imports: [UpperCasePipe],
})
export class App {
  username = 'yOunGTECh';
}