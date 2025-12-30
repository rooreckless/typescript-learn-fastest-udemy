import { Component,signal } from '@angular/core';

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
  }
  protected logAlert(): void {
    alert('Warning button was clicked!');
  }
  protected changeTitle(): void {
    this.title.set("CHANGED--- My Recipe Box");
  }
}
