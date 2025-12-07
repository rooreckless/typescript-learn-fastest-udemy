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
import {Child} from './child';

@Component({
  // 親コンポーネントでは、addItemEventを受け取ったら、addItemメソッドを呼び出す
  // items配列の長さの描画と、items配列内要素を繰り返し表示する
  // = 子コンポーネントのボタンが押されると、子コンポーネントからイベントで'🐢'が送信され、
  // 親コンポーネントのitems配列に追加されて描画に利用される
  selector: 'app-root',
  template: `
    <app-child (addItemEvent)="addItem($event)" />
    <p>🐢 all the way down {{ items.length }}</p>
    <span>@for(item of items; track item){{{item}}}</span>
  `,
  imports: [Child],
})
export class App {
  items = new Array();

  // addItemEventで受け取ったときに実行されるメソッド
  // addItemメソッドは、受け取った文字列をitems配列に追加する
  addItem(item: string) {
    this.items.push(item);
  }
}

