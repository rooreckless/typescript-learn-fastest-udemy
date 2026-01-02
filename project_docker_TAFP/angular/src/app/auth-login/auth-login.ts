import { Component,inject } from '@angular/core';
import { ReactiveFormsModule, FormBuilder, FormGroup, Validators} from '@angular/forms';
import { AuthService } from '../services/auth';
import { Router } from '@angular/router';
@Component({
  selector: 'app-auth-login',
  imports: [ReactiveFormsModule],
  templateUrl: './auth-login.html',
  styleUrl: './auth-login.css',
})
export class AuthLogin {
  // fb = FormBuilderのインスタンス、はフォームの構造を定義するための準備
  private fb = inject(FormBuilder);
  private authService = inject(AuthService);
  // ログイン後に自動的にリダイレクトするためのRouterも注入
  private router = inject(Router);
  // loginFormはFormGroupのインスタンス、フォーム全体を表す
  protected loginForm: FormGroup = this.fb.group({
    // フォームの各フィールドとそのバリデーションルールを定義
    email: ['', [Validators.required, Validators.email]],
    password: ['', [Validators.required, Validators.minLength(6)]],
  })

  // フォームの送信処理(送信ボタンが押された時に実行される)
  protected onSubmit(): void {
    if (this.loginForm.valid) {
      // フォームが有効(=バリデーションチェックにすべて成功)な場合
      const email: string = this.loginForm.value.email;
      const password: string = this.loginForm.value.password;
      
      // AuthServiceを使ってログインを試みる
      this.authService.login(email, password).subscribe({
        next: (response) => {
          console.log('Login Successful:', response);
          // 取得したトークンを保存
          this.authService.saveToken(response.access_token);
          // ログイン成功後にホームページへリダイレクト
          this.router.navigate(['/home']);
        },
        error: (error) => {
          console.log('Login Failed:', error);
        }
      });
      
    } else {
      // フォームが無効な場合、エラーメッセージをコンソールに出力
      console.log('Form is invalid');
    }
  }
}
