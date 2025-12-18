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
import {Car} from './car';
@Component({
  selector: 'app-root',
  template: `
  <p>{{car.getCars()}}</p>
    `,
  imports: [],
})
export class App {
  // car.tsからCarクラスをインポートしてインスタンス化 <- 依存がある状態
  car = new Car();
}

