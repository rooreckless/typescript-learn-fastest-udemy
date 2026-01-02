import { Component,inject,signal,NgModule } from '@angular/core';
import { ReactiveFormsModule, FormBuilder, FormGroup, Validators} from '@angular/forms';
import { AsyncPipe } from '@angular/common';
import { CategoryService } from '../services/category';
import { Subject, switchMap } from 'rxjs';
import { FormsModule } from '@angular/forms';
@Component({
  selector: 'app-category-form',
  imports: [FormsModule,AsyncPipe],
  templateUrl: './category-form.html',
  styleUrl: './category-form.css',
})
export class CategoryForm {
    // // fb = FormBuilderのインスタンス、はフォームの構造を定義するための準備
    // private fb = inject(FormBuilder);
    
    // 送信トリガー
    private submit$ = new Subject<any>();

    result$ = this.submit$.pipe(
      switchMap(formValue =>
        this.categoryService.createCategory(formValue)
      )
    );
    // フォームの内容をPOSTするためのCategoryServiceを注入
    constructor(private categoryService :CategoryService){}
    
    // // categoryFormはFormGroupのインスタンス、フォーム全体を表す
    // protected categoryForm: FormGroup = this.fb.group({
    //   // フォームの各フィールドとそのバリデーションルールを定義
    //   name: ['', [Validators.required, Validators.minLength(3)]],
    // })
    // error_message=signal<string>('');

    
    // ⭐ async pipe 用 Observable
    // swithMapがPOSTを実行し、その結果をresult$が受け取る
    

    onSubmit(formValue: any) {
      this.submit$.next(formValue);
    }
}
