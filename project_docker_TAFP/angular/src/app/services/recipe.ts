import { Injectable,signal } from '@angular/core';
import {RecipeModel,Ingredient} from '../models';
import {RecipeDetail} from '../recipe-detail/recipe-detail';
import {MOCK_RECIPES} from '../mock-recipes';

@Injectable({
  providedIn: 'root',
})
export class RecipeService {
  //Module 14: Services & Dependency Injection (DI)

  //RecipeListコンポーネントでMOCK_RECIPESを直接使うのではなく、このサービス経由でアクセスするようにする
  private readonly recipes = signal<RecipeModel[]>(MOCK_RECIPES);

  //RecipeListコンポーネントで、レシピの全取得メソッドや、ID検索メソッドを実装しないですむようにする
  // 共通で使う可能性が高いメソッドなので、inject()だけでつかえるようになり、
  // 使う側のRecipeListコンポーネント側がこれらのメソッドの実装内容までしる必要がなくなる。
  public getAllRecipes(): RecipeModel[] {
    return this.recipes();
  }
  
  public getRecipeById(id: number): RecipeModel | undefined {
    return this.recipes().find((recipe: RecipeModel) => recipe.id === id);
  }
  
  public searchRecipes(query: string): RecipeModel[] {
    //大文字小文字を区別しない検索にする
    // 入力された文字列を小文字にする
    const lower_query = query.toLowerCase();
    
    // return this.recipes().filter((recipe: RecipeModel) => recipe.name.includes(query));
    return this.recipes().filter((recipe: RecipeModel) => {
      // ↑のprivateなrecipesの配列内オブジェクトのnameプロパティを小文字に変換してから、
      // その文字列の中でlower_queryを含むオブジェクトを返す
      return recipe.name.toLowerCase().includes(lower_query)
    });
  }
}
