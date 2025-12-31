import { Component, inject } from '@angular/core';
import { ReactiveFormsModule, FormBuilder, FormGroup, Validators, FormArray } from '@angular/forms';
import { Router } from '@angular/router';
import { RecipeService } from '../services/recipe';
import { RecipeModel } from '../models';

@Component({
  selector: 'app-recipe-form',
  imports: [ReactiveFormsModule],
  templateUrl: './recipe-form.html',
  styleUrl: './recipe-form.css',
})
export class RecipeForm {
  // fb = FormBuilderのインスタンス、はフォームの構造を定義するための準備
  private fb = inject(FormBuilder);
  private router = inject(Router);
  private recipeService = inject(RecipeService);
  
  // receipeFormはFormGroupのインスタンス、フォーム全体を表す
  protected receipeForm: FormGroup = this.fb.group({
    // フォームの各フィールドとそのバリデーションルールを定義
    name: ['', [Validators.required, Validators.minLength(3)]],
    description: ['', [Validators.required]],
    // ingredientsはFormArrayとして初期化、空の配列で開始し、後で動的に材料を追加(いくらでも追加)できるようにする
    ingredients: this.fb.array([]),
    // imgUrlフィールドには、必須バリデーションとURL形式のパターンバリデーションを追加
    imgUrl: ['', [Validators.pattern(/^(https?:\/\/.*\.(?:png|jpg|jpeg|gif|svg|webp))$/i)]],
    // isFavoriteフィールドはチェックボックス用として定義、初期値はfalse
    isFavorite: [false],
  })

  // フォームの送信処理(送信ボタンが押された時に実行される)
  protected onSubmit(): void {
    if (this.receipeForm.valid) {
      // フォームが有効(=バリデーションチェックにすべて成功)な場合
      const newRecipe: RecipeModel = this.receipeForm.value as RecipeModel;
      
      // RecipeServiceを使ってレシピを保存
      this.recipeService.addRecipe(newRecipe);
      
      console.log('Recipe Submitted:', newRecipe);
      
      // レシピ一覧ページにリダイレクト
      this.router.navigate(['/recipes']);
    } else {
      // フォームが無効な場合、エラーメッセージをコンソールに出力
      console.log('Form is invalid');
    }
  }
  // FormArrayにアクセスすすためのgetter
  get ingredients(){
    return this.receipeForm.get('ingredients') as FormArray;
  }

  // receipFormに、ingredientsを追加するメソッド
  addIngredient():void{

    console.log("addIngredient called");
    this.ingredients.push(this.fb.group({
      name: ['', Validators.required],
      quantity: [0, [Validators.required, Validators.min(0.01)]],
      unit: ['', Validators.required],
    }));

    console.log(this.ingredients)
  }
  // receipFormに、ingredientsを削除するメソッド
  removeIngredient(index: number):void{
    this.ingredients.removeAt(index);
  }
}
