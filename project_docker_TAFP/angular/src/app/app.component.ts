import { Component,signal} from '@angular/core';
import {RecipeList} from './recipe-list/recipe-list';

@Component({
  selector: 'app-root',
  standalone: true,
  // templateUrlをいれたことで、htmlは外部ファイルにした
  templateUrl: './app.component.html',
  // styleUrls配列をいれたことで、cssは外部ファイルにした上で、複数導入できる
  styleUrls: ['./app.component.css'],
  //↑でimportした子コンポーネントは、ここでもimportsする必要がある
  imports: [RecipeList],
})
// クラス名はAppにする必要があり、↑のselectorも'app-root'にする必要がある
export class App {
  // signalには文字列を入れることもできるし、テンプレートで{{ title() }}のように表示するのも一緒
  // (protected readonlyを使へばテンプレートからのみアクセス可能でより安全になるが、それは状況しだい)
  title = signal("My Recipe Box");

  
}