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
  // さらに追加で、spanタグのstyle属性のcolorプロパティにバインドしてみる = プロパティの文字列で色を変えられる
  template: `
    <div [contentEditable]="isEditable">
    <span [style.color] = "colorString">
      aaa
    </span>
    
    </div>
  `,
})
export class App {
  // boolean型プロパティを定義
  isEditable: boolean = false;

  // string型プロパティを定義
  colorString: string = '#00ff00';
}



