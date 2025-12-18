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

// 依存性注入(サービスをnewしなくても使えるようにする)にはinfectもインポート
import {Component,inject} from '@angular/core';
import {CarService} from './car.service';
@Component({
  selector: 'app-root',
  template: `
  <p>carService.getCars() = {{carService.getCars()}}</p><br>
  <p>display = {{display}}</p>
    `,
  imports: [],
})
export class App {
  // car.service.tsからCarServiceクラスを注入
  // =インスタンス化しなくていい <- 依存性(サービス)を注入してきた状態
  carService = inject(CarService);
  // インスタンス火していないけど、そのままサービスのメソッド(getCars)を使えている
  display = this.carService.getCars().join("☆");
}

