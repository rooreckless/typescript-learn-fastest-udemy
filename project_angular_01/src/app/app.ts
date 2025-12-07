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
  // テンプレートのsection部分にマウスオーバーで秘密のメッセージを表示する
  template: `  
    <section (mouseover)="showSecretMessage()">
      There's a secret message for you, hover to reveal 👀
      {{ message }}
    </section>
  `,
})
export class App {
  message = '';
  // ただの関数だが、テンプレートのイベントにバインドさせて、イベントハンドラとする
  showSecretMessage() {
    this.message = 'Angular is awesome! 🚀';
  }
}




