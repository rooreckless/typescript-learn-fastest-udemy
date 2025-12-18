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

// コンストラクタベースでの依存性注入(サービスをnewしなくても使えるようにする)にはinjectはなくてもいい
import {Component} from '@angular/core';
import {CarService} from './car.service';
@Component({
  selector: 'app-root',
  template: `
  <p>display = {{display}}</p>
    `,
  imports: [],
})
export class App {
  // injectを使う場合(Angular14以降)
  // carService = inject(CarService);
  display: string;

  // -----
  // car.service.tsからCarServiceクラスをコンストラクタベースで注入(古いAngularでのやり方)
  constructor(private carService: CarService) {
    this.display = this.carService.getCars().join(' ⭐️ ');
  }
  // ただし、このやり方だと、carServiceはprivateなので、
  // テンプレート内で直接carService.getCars()などは使えなくなる。
  // -----


  // injectを使う場合が以下のようになる。
  // display = this.carService.getCars().join("☆");
}

