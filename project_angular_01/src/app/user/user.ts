
import {Component} from '@angular/core';
// favotiteFrameworkプロパティを追加し、それをpタグとしてtemplateに表示するように変更
// また、labelタグも追加しているが、input要素は追加していない。
@Component({
  selector: 'app-user',
  template: `
    <div>Username: {{ username }}</div>
    <p>{{ username }}'s favorite framework: {{ favoriteFramework }}</p>
    <label for="framework">Favorite Framework:</label>
  `,
})
export class User {
  username = 'youngTech';
  favoriteFramework = '';
}
