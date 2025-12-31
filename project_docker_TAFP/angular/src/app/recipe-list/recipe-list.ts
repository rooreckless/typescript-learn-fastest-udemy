import { Component,signal,computed} from '@angular/core';
import {RecipeModel,Ingredient} from '../models';
import {RecipeDetail} from '../recipe-detail/recipe-detail';
import {MOCK_RECIPES} from '../mock-recipes';
@Component({
  selector: 'app-recipe-list',
  imports: [RecipeDetail],
  templateUrl: './recipe-list.html',
  styleUrl: './recipe-list.css',
})
export class RecipeList {
  // Module4: State Management with Writable Signals (Part 1: set)
  // signalで管理するオブジェクトとしてRecipeModelを使う)
  recipes = signal<RecipeModel[]>(MOCK_RECIPES);
  // 表示用のsignalがrecipe
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
    const nextRecipe = this.recipes().find((recipe: RecipeModel) => recipe.id === nextId);
    // ちゃんとnextRecipeが見つかった場合のみ、recipe signalの値を更新する
    // signalの値を更新するには(protected readonlyをつけていない場合は)recipe.set(...)メソッドを使う
    if (nextRecipe) {
      this.recipe.set(nextRecipe);
    }
  }

  protected change_recipe_to1(): void {
    const nextRecipe = this.recipes().find((recipe: RecipeModel) => recipe.id === 1);
    if (nextRecipe) {
      this.recipe.set(nextRecipe);
    }
  }

  protected change_recipe_to2(): void {
    const nextRecipe = this.recipes().find((recipe: RecipeModel) => recipe.id === 2);
    if (nextRecipe) {
      this.recipe.set(nextRecipe);
    }
  }
  
  
}
