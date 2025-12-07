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
  // テンプレート内で@for文を使い、users配列の要素ごとに描画する
  // track句で各要素の一意な識別子を指定する(trackの指定は必須)
  template: `
  usersリスト: <br>
  @for(user of users; track user.id){
    <div>user.id = {{user.id}}: user.name = {{user.name}}</div>
  }
  `,
})
export class App {
  // 配列(中がオブジェクト)なプロパティusersを定義
  users:Array<{id:number,name:string}> = [
    {id:0,name:'山田太郎'},
    {id:1,name:'鈴木花子'},
    {id:2,name:'佐藤次郎'},
    {id:3,name:'田中三郎'},
  ];
}


