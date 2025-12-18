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
  username | uppercase = {{ username | uppercase }}<br>
  <hr>
  <ul>
      <li>Number {{ num }}</li>
      <li>Date  {{ birthday }}</li>
      <li>Currency  {{ cost }}</li>
  </ul>
  <ul>
      <li>Number with "decimal" {{ num }}</li>
      <li>Date with "date" {{ birthday }}</li>
      <li>Currency with "currency" {{ cost }}</li>
  </ul>
  `,
  imports: [UpperCasePipe],
})
export class App {
  username = 'yOunGTECh';
  num = 103.1234;
  birthday = new Date(2023, 3, 2);
  cost = 4560.34;
}