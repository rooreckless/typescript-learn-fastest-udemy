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
// いろんなパイプを使うため追加import
import {DecimalPipe, DatePipe, CurrencyPipe} from '@angular/common';

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
  <hr>
  <ul>
      <li>Number with "decimal" {{ num | number:"3.2-2" }}<br>
      ↑ DecimalPipeのnumberに"3.2-2"を引数として渡したうえで、変数numを変換している</li>
      <li>Date with "date" {{ birthday | date: 'medium' }}<br>
      ↑ DatePipeのdateに'medium'を引数として渡したうえで、変数birthdayを変換している</li>
      <li>Currency with "currency" {{ cost | currency}}<br>
      ↑ CurrencyPipeのcurrencyを使って、変数costを変換している</li>
  </ul>
  `,
  imports: [UpperCasePipe,DecimalPipe, DatePipe, CurrencyPipe],
})
export class App {
  username = 'yOunGTECh';
  num = 103.1234;
  birthday = new Date(2023, 3, 2);
  cost = 4560.34;
}