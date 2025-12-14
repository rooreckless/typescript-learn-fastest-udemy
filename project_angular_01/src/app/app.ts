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
//リアクティブフォームモジュールたちをインポート
// 【追加】Validatorsもインポート
import { ReactiveFormsModule, FormControl, FormGroup,Validators } from '@angular/forms';
//formタグの中は、label内でinputな点は一緒だが、inputで双方向バインディングしていない。
//formControlNameディレクティブを使って、フォームコントロールとinput要素を関連付けている。
@Component({
  selector: 'app-root',
  // フォームタグには、formGroup属性についてはプロパティバインディングを使い、profileFormフォームグループをバインドしている。
  // buttonタグ自体に(click)イベントで実行関数を指定してもいいが、
  // 今回はformタグの(ngSubmit)イベントでonSubmit()関数を指定している。(結果は一緒) 
  template: `
    <form [formGroup]="profileForm" (ngSubmit)="onSubmit()">
      <label>
        Name
        <input type="text" formControlName="name" />
      </label>
      <label>
        Email
        <input type="email" formControlName="email" />
      </label>
      <button type="submit">Submit</button>
    </form>
    <hr/>
    <h2>Profile Form</h2>
    <p>Name: {{ profileForm.value.name }}</p>
    <p>Email: {{ profileForm.value.email }}</p>
  `,
  // ↑フォームに入力さらた値は、formGroup属性にバインドされた変数.value.プロパティ名で取得できる。
  imports: [ReactiveFormsModule],
})
export class App {
  //フォームグループを作成し、inputタグのformControlNameのnameとemailのフォームコントロールを追加
  profileForm = new FormGroup({
    // 以下はフォームタグ内のinputタグで使われているformControlNameと一致させる必要がある。
    // 【追加】FormControlにValidators.requiredを追加して、必須入力にする。
    // 【追加】さらに、email入力箇所については、Validators.emailも追加して、メールアドレス形式のバリデーションを行うようにすることもできる。
    name: new FormControl('', Validators.required),
    email: new FormControl('', [Validators.required, Validators.email]),
  });

  onSubmit() {
    alert(this.profileForm.value.name + "--" + this.profileForm.value.email);
  }
}

