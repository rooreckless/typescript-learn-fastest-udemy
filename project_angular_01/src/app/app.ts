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
  // テンプレートで@if-@else構文を使用
  // Appコンポーネントのbooleanなプロパティで切り替える
  template: `
    @if(isServerRunning){
    <span>Yes, the server is running</span>
    }
    @else{
    <span>No, the server is <span class="not">NOT</span> running</span>
    }    
  `,
  // if文のどっちかがわかりやすくなるようスタイルを指定
  styles: [`
    .not {
      color: red;
      font-weight: bold;
    }
  `]
})
export class App {
  // boolean型プロパティを作成(手動でtrue/falseを切り替えて挙動確認をする)
  isServerRunning: boolean = false;
}

