import { Component,signal} from '@angular/core';
//ルーティング有効化する設定
import { RouterOutlet, RouterLink } from '@angular/router';

@Component({
  selector: 'app-root',
  // templateUrlをいれたことで、htmlは外部ファイルにした
  templateUrl: './app.component.html',
  // styleUrls配列をいれたことで、cssは外部ファイルにした上で、複数導入できる
  styleUrls: ['./app.component.css'],
  //↑でimportした子コンポーネントは、ここでもimportsする必要がある
  // 今回はルーティングを有効化するためにRouterOutletとRouteLinkをimportsに追加
  imports: [RouterOutlet, RouterLink],
})
// クラス名はAppにする必要があり、↑のselectorも'app-root'にする必要がある
export class App {
  // signalには文字列を入れることもできるし、テンプレートで{{ title() }}のように表示するのも一緒
  // (protected readonlyを使へばテンプレートからのみアクセス可能でより安全になるが、それは状況しだい)
  title = signal("My Recipe Box");

  
}