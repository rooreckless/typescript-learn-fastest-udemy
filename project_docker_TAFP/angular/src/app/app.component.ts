import { Component,signal } from '@angular/core';
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
  // Module2: Dynamic Text with Interpolationとsignalを使って状態管理を行う 参考 https://zenn.dev/rdlabo/articles/4b23117adb33aa
  // protected readonlyをつけた変数は、コンポーネントのテンプレートから「のみ」アクセス可能にする
  // テンプレートでは{{ count() }}のように関数呼び出しの形でアクセスする
  protected readonly count = signal(0);
  // signalには文字列を入れることもできるし、テンプレートで{{ title() }}のように表示するのも一緒
  // (protected readonlyを使へばテンプレートからのみアクセス可能でより安全になるが、それは状況しだい)
  title = signal("My Recipe Box");

  // Module3: Event Listeners ボタンがクリックされたときに呼び出されるメソッド
  // 以下のlogInfoが、htmlでは、<button (click)= "logInfo()">と書いてあれば、それをクリックすると呼び出される
  // protectedをつけたメソッドは、コンポーネントのテンプレートから「のみ」アクセス可能にする　= tsファイルからはアクセスできない
  protected logInfo(): void {
    console.log('Info button was clicked!');
  };
  protected logAlert(): void {
    alert('Warning button was clicked!');
  };
  protected changeTitle(): void {
    this.title.set("CHANGED--- My Recipe Box");
  };
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