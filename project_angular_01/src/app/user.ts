import {Component, input} from '@angular/core';

@Component({
  selector: 'app-user',
//   コンポーネント入力プロパティnameの描画
  template: `
    <p>The user's name is {{ name() }}</p>
  `,
})
export class User {
    // nameは外部(このコンポーネントではなく、親コンポーネント)から
    // 値を受け取る「コンポーネント入力プロパティ」
    name = input<string>('');
}
