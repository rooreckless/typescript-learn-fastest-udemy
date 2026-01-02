import { Component,inject,signal } from '@angular/core';
import { ReactiveFormsModule, FormBuilder, FormGroup, Validators} from '@angular/forms';
import { UserService } from '../services/user';
import { Router } from '@angular/router';
// import { HttpErrorResponse } from '@angular/common/http';
// POSTリクエストをする場合の解決策2としてfirstValueFromをインポート
import { firstValueFrom } from 'rxjs';
@Component({
  selector: 'app-user-form',
  imports: [ReactiveFormsModule],
  templateUrl: './user-form.html',
  styleUrl: './user-form.css',
})
export class UserForm {
  // fb = FormBuilderのインスタンス、はフォームの構造を定義するための準備
  private fb = inject(FormBuilder);
  private userService = inject(UserService);
  private router = inject(Router);

  // userFormはFormGroupのインスタンス、フォーム全体を表す
  protected userForm: FormGroup = this.fb.group({
    // フォームの各フィールドとそのバリデーションルールを定義
    name: ['', [Validators.required, Validators.minLength(3)]],
    email: ['', [Validators.required, Validators.email]],
    password: ['', [Validators.required, Validators.minLength(6)]],
    admin: [false],
  })
  error_message=signal<string>('');
  // フォームの送信(POST)処理(送信ボタンが押された時に実行される)方法1: subscribeを使う方法
  protected onSubmit_sol1(): void {
    if (this.userForm.valid) {
      // フォームが有効(=バリデーションチェックにすべて成功)な場合
      const newUser = this.userForm.value;
      console.log('User Submitted:', newUser);
      // --- バックエンドのユーザー作成APIを呼び出す---
      // ↓だと失敗する
      // this.userService.createUser(newUser);
      // 解決策1 : subscribeでレスポンスを受け取る必要があります。
      this.userService.createUser(newUser).subscribe({
        next: (response) => {
          console.log('User Created Successfully:', response);
          // ユーザー一覧ページにリダイレクト
          this.router.navigate(['/users']);
        },
        error: (error) => {
          console.log('User Creation Failed:', error);
          this.error_message.set('User Creation Failed: ' + error.status + ' ' + error.statusText + ' ' + error.error.detail);
        }
      });

      
    } else {
      // フォームが無効な場合、エラーメッセージをコンソールに出力
      console.log('Form is invalid');

    }
  }
  // --↑↓どっちの方法でPOSTリクエストしたいか、選んだら、html側の(クリックイベント)も対応させること--
  // フォームの送信(POST)処理(送信ボタンが押された時に実行される)方法2: async/awaitと、firstValueFromを使う方法
  protected async onSubmit_sol2(): Promise<void> {
    if (this.userForm.valid) {
      // フォームが有効(=バリデーションチェックにすべて成功)な場合
      const newUser = this.userForm.value;
      console.log('User Submitted:', newUser);
      // --- バックエンドのユーザー作成APIを呼び出す---

      // 解決策2 : firstValueFromを使う方法。
      try {
        const response = await firstValueFrom(this.userService.createUser(newUser));
        console.log('User Created Successfully:', response);
        // ユーザー一覧ページにリダイレクト
        this.router.navigate(['/users']);
      } catch (error: any) {
        console.log('User Creation Failed:', error);
        this.error_message.set('User Creation Failed: ' + error.status + ' ' + error.statusText + ' ' + error.error.detail);
      }

    } else {
      // フォームが無効な場合、エラーメッセージをコンソールに出力
      console.log('Form is invalid');
    }
  }

  
}
