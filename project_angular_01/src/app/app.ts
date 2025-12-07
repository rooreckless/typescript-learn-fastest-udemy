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
  // ボタンをクリックするとメッセージを表示/非表示切り替え
  template: `  
    <section (mouseover)="showSecretMessage()">
      There's a secret message for you, hover to reveal 👀
      {{ message }}
    </section>
    <br>
    <button (click)="showSecretMessage2()">Show Secret Message / Delete Message</button>
    <div>@if(isButtonClicked){{{message2}}}
      
    </div>
  `,
})
export class App {
  message:string = '';
  message2:string = "Clicked! 🎉";
  isButtonClicked:boolean= false;
  
  // ただの関数だが、テンプレートのイベントにバインドさせて、イベントハンドラとする
  showSecretMessage() {
    this.message = 'Angular is awesome! 🚀';
  }

  showSecretMessage2(){
    if(this.isButtonClicked){
      this.isButtonClicked = false;
    }else{
      this.isButtonClicked = true;
    }
  }
}




