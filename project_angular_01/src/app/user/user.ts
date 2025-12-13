
import {Component} from '@angular/core';
// FormsModuleをインポート
import {FormsModule} from '@angular/forms';
// inputタグの[(ngModel)]で双方向バインディングになる
@Component({
  selector: 'app-user',
  template: `
    <div>Username: {{ username }}</div>
    <p>{{ username }}'s favorite framework: {{ favoriteFramework }}</p>
    <label for="framework">
      好きなフレームワーク:
      <input id="framework" type="text" [(ngModel)]="favoriteFramework" />
    </label>
    <hr/>
    <button (click)="showFramework()">Show Framework</button>
  `,
  // 上でインポートしたら、@Componentsのimportsにも追加する
  imports: [FormsModule],
})
export class User {
  username = 'youngTech';
  favoriteFramework = '';
  // ボタンにclickイベントが発生したときに呼び出されるメソッド
  // 特にinputタグで双方向バインディングしたfavoriteFrameworkの値をアラートで表示するのが目的
  showFramework(){
    alert(`${this.username}さんの好きなフレームワークは${this.favoriteFramework}です。`);
  };
}
