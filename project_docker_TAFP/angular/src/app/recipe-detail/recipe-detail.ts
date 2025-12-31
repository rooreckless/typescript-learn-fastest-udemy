import { Component, computed, signal, inject, OnInit } from '@angular/core';
import { RecipeModel, Ingredient } from '../models';
import { ActivatedRoute, Router } from '@angular/router';
import { RecipeService } from '../services/recipe';

@Component({
  selector: 'app-recipe-detail',
  imports: [],
  templateUrl: './recipe-detail.html',
  styleUrl: './recipe-detail.css',
})
export class RecipeDetail implements OnInit {
  // Module 15: Basic Routing
  // URLパラメータ(パスパラメータ)からIDを取得し、RecipeServiceからデータを取得する
  private route = inject(ActivatedRoute);
  private router = inject(Router);
  private recipeService = inject(RecipeService);
  
  // input()からsignalに変更（親から受け取らず、自分で取得）
  protected readonly recipe = signal<RecipeModel | null>(null);
  
  // Module 5: State Management with Writable Signals (Part 2: update)
  // このコンポーネント内だけで使うsignalなら、protectedは使用できる。
  protected readonly servings = signal(1);
  
  ngOnInit(): void {
    // URLパラメータ(パスパラメータ)からIDを取得
    const id = Number(this.route.snapshot.paramMap.get('id'));
    // RecipeServiceからレシピを取得
    const foundRecipe = this.recipeService.getRecipeById(id);
    
    if (foundRecipe) {
      this.recipe.set(foundRecipe);
    } else {
      // レシピが見つからない場合は一覧に戻る
      this.router.navigate(['/recipes']);
    }
  }

  protected incrementCount(): void{
    // signalの値を更新するには(protected readonlyをつけていない場合は)servings.update(...)メソッドを使う
    // .setと.updateの違いは、.setは新しい値を直接セットするのに対し、
    // .updateは現在の値を引数として受け取り、その現在の値を使って新しい値を返す「関数」を渡す点にある
    this.servings.update((current_value: number) => current_value + 1);
  }
  protected decrementCount(): void{
    // servings.update(...)メソッドを使って値をデクリメントするが、1未満にはならないようにする
    this.servings.update((current_value: number) => {
      if (current_value <= 1){
        return 1;
      }
      return current_value - 1
    });
  }

  // Module 6: Computed Signals
  // レシピの材料と人数から、調整された材料の量を計算する
  protected readonly adjustedIngredients = computed(() => {
    const currentRecipe = this.recipe();
    // nullチェック：レシピがまだ読み込まれていない場合は空配列を返す
    if (!currentRecipe) return [];
    
    const currentServings = this.servings();
    
    // 各材料の量を現在の人数に基づいて調整
    return currentRecipe.ingredients.map((ingredient: Ingredient) => ({
      ...ingredient,  // 全てのプロパティをコピー
      quantity: ingredient.quantity * currentServings  // quantityだけ上書き
    }));
  });


}
