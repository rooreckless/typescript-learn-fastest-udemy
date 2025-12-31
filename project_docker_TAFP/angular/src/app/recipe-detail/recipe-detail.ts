import { Component, input, computed,signal } from '@angular/core';
import {RecipeModel,Ingredient} from '../models';
@Component({
  selector: 'app-recipe-detail',
  imports: [],
  templateUrl: './recipe-detail.html',
  styleUrl: './recipe-detail.css',
})
export class RecipeDetail {
  // 親コンポーネントからrecipeプロパティを受け取る(pretectedにはできない)
  // input()で作成されたプロパティは親からバインディングする必要があるため、protectedにはできない
  readonly recipe = input.required<RecipeModel>();
  // Module 5: State Management with Writable Signals (Part 2: update)
  //このコンポーネント内だけで使うsignalなら、protectedは使用できる。
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
