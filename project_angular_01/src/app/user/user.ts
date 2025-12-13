
import {Component} from '@angular/core';
// FormsModuleをインポート
import {FormsModule} from '@angular/forms';

@Component({
  selector: 'app-user',
  template: `
    <div>Username: {{ username }}</div>
    <p>{{ username }}'s favorite framework: {{ favoriteFramework }}</p>
    <label for="framework">
      好きなフレームワーク:
      <input id="framework" type="text" />
    </label>
  `,
  // 上でインポートしたら、@Componentsのimportsにも追加する
  imports: [FormsModule],
})
export class User {
  username = 'youngTech';
  favoriteFramework = '';
}
