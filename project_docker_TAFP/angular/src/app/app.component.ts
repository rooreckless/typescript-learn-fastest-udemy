import { Component,signal,computed } from '@angular/core';
import {RecipeModel,Ingredient} from './models';
import {MOCK_RECIPES} from './mock-recipes';

@Component({
  selector: 'app-root',
  standalone: true,
  // templateUrlをいれたことで、htmlは外部ファイルにした
  templateUrl: './app.component.html',
  // styleUrls配列をいれたことで、cssは外部ファイルにした上で、複数導入できる
  styleUrls: ['./app.component.css']
})
// クラス名はAppにする必要があり、↑のselectorも'app-root'にする必要がある
export class App {
  // signalには文字列を入れることもできるし、テンプレートで{{ title() }}のように表示するのも一緒
  // (protected readonlyを使へばテンプレートからのみアクセス可能でより安全になるが、それは状況しだい)
  title = signal("My Recipe Box");

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
  // Module 5: State Management with Writable Signals (Part 2: update)
  protected readonly servings = signal(1);

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
  // Module 6: Computed Signals = setやupdateで値を変更するsignalとは別に、
  // 他のsignalの値に基づいて自動的に更新されるsignalを作成する
  //   例えば:

  // - 商品の価格と税率から、税込価格を計算する
  // - レシピの材料と人数から、調整された材料の量を計算する
  // - 複数の入力フィールドから、合計を計算する
  // まずcomputedをimportして変数定義し、computedの無名関数ないで他のsignalの値を使って計算を行う
  // ここでは、レシピの材料と人数から、調整された材料の量を計算する例を示す
  protected readonly adjustedIngredients = computed(()=>{
    // 現在の人数(signalから)を取得
    const current_servings=this.servings();
    // 現在のレシピの材料(=表示しているrecipeのsignalから)を取得
    const current_recipe=this.recipe();

    // current_recipe.ingredientsの各材料の量quantityを現在の人数に基づいて調整する
    // 書き方1
    // return current_recipe.ingredients.map((ingredient: Ingredient)=>({
    //   ...ingredient,  // 全てのプロパティをコピー
    //   quantity: ingredient.quantity * current_servings  // quantityだけ上書き
    // }));

    // 書き方2
    return current_recipe.ingredients.map((ingredient: Ingredient)=>{
      return {
        ...ingredient,  // 全てのプロパティをコピー
        quantity: ingredient.quantity * current_servings  // quantityだけ上書き
      };
    });
    // mapメソッドは新しい配列を返す(=current_recipe.ingredients自体を書き換えるわけではない)
    // ので、そのままreturnで返す
    // さらにmapの引数は無名関数であり、最終的にオブジェクトを返したいのでreturn {...}の形にする必要がある
    // その無名関数のreturn {...}の中でスプレッド構文を使い、元のingredientオブジェクトの全プロパティをコピーしつつ、
    // quantityプロパティだけを上書きしている
    // これにより、元のingredientオブジェクトは変更せずに、新しいオブジェクトを作成している
    // https://qiita.com/NNNiNiNNN/items/3743ce6db31a421d88d0
  });
}