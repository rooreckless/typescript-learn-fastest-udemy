// app.routes.tsで定義した'user'ルートに対応するUserコンポーネント
// 内容はチュートリアルからのコピーです。
import {Component} from '@angular/core';

@Component({
  selector: 'app-user',
  template: `
    <div>Username: {{ username }}</div>
  `,
})
export class User {
  username = 'youngTech';
}
