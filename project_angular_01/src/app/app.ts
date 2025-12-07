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
  styleUrls: ['app.css'],
  // テンプレートのdivタグのcontentEditable属性にバインドしてみる
  // trueが入ると編集可能で描画される
  template: `
    <div [contentEditable]="isEditable">
    aaa
    </div>
  `,
})
export class App {
  // boolean型プロパティを定義
  isEditable: boolean = false;
}



