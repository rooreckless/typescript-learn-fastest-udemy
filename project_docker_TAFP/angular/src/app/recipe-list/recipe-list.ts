import { Component,signal,computed,inject} from '@angular/core';
// 双方向バインディングのためにインポート
import { FormsModule } from '@angular/forms';
import {RecipeService} from '../services/recipe';
import {RecipeModel} from '../models';
import {RecipeDetail} from '../recipe-detail/recipe-detail';
@Component({
  selector: 'app-recipe-list',
  imports: [RecipeDetail, FormsModule],
  templateUrl: './recipe-list.html',
  styleUrls: ['./recipe-list.css'],
})
export class RecipeList {
  private recipeService = inject(RecipeService); // DIで注入
  
  recipes = signal<RecipeModel[]>(this.recipeService.getAllRecipes());
  recipe = signal<RecipeModel>(this.recipes()[0]);
  
  protected nextRecipe(): void {
    // signalで管理しているオブジェクトのプロパティにアクセスするには、signal名()のように関数呼び出しの形でアクセスする
    // それを使い、現在表示しているrecipeのidを取得してcurrentIdに入れる    
    const currentId = this.recipe().id;
    // 次に表示するレシピのidをcurrentIdから計算する。最後のレシピの場合は最初のレシピに戻るようにする
    // 具体的には、nextIdは「currentIdがMOCK_RECIPESの長さと同じ場合は1に戻し」、
    // 「そうでない場合はcurrentIdに1を足した値をnextIdにいれる」
    const nextId = currentId === this.recipes().length ? 1 : currentId + 1;
    // 次にrecipeとして表示するレシピをMOCK_RECIPES配列内オブジェクトのうち、idとnextIdが一致するから探してくる
    const nextRecipe = this.recipeService.getRecipeById(nextId);
    // ちゃんとnextRecipeが見つかった場合のみ、recipe signalの値を更新する
    // signalの値を更新するには(protected readonlyをつけていない場合は)recipe.set(...)メソッドを使う
    if (nextRecipe) {
      this.recipe.set(nextRecipe);
    }
  }

  protected change_recipe_to1(): void {
    // const nextRecipe = this.recipes().find((recipe: RecipeModel) => recipe.id === 1);
    const nextRecipe = this.recipeService.getRecipeById(1);
    if (nextRecipe) {
      this.recipe.set(nextRecipe);
    }
  }

  protected change_recipe_to2(): void {
    // const nextRecipe = this.recipes().find((recipe: RecipeModel) => recipe.id === 2);
    const nextRecipe = this.recipeService.getRecipeById(2);
    if (nextRecipe) {
      this.recipe.set(nextRecipe);
    }
  }
  
  // Module 13: Two-Way Binding (双方向バインディング)
  // 検索用の文字列格納signal(双方向バインディングはts側は普通)
  search_text_for_recipe = signal<string>('');
  // インクリメンタルサーチの結果用のcomputed signalのsearch_result_recipe : htmlでは{{search_result_recipe()}}で表示できる。
  search_result_recipe = computed(()=>{
    // 入力された検索文字列を取得
    const inputed_text = this.search_text_for_recipe();
    // signalのrecipes配列にフィルターをかけて、新しいオブジェクトを返す
    // 配列内オブジェクトのnameプロパティにinputed_textが含まれているかどうかでフィルターをかける
    // const filtered_recipes = this.recipes().filter((recipe : RecipeModel)=>{
    //   return recipe.name.includes(inputed_text);  
    // })
    const filtered_recipes = this.recipeService.searchRecipes(inputed_text);

    if (filtered_recipes.length !== 1){
      // 1件に特定できなかった場合は表示しないようにnullを返す
      return null;
    }
    console.log('Filtered Recipes[0]:', filtered_recipes[0]);
    return filtered_recipes[0];
  });
}
