import {Component} from '@angular/core';
// 画像最適化のため見NgOptimizedImageをインポート
import {NgOptimizedImage} from '@angular/common';
@Component({
  selector: 'app-user',
  template: `
    <p>Username: {{ username }}</p>
    <p>Preferred Framework:</p>

    <ul>
    <li>
        普通のimgタグ こっちでも表示可能だしサイズ調整できる
        <img src="/assets/logo.svg" alt="Angular logo" width="32" height="32" />
    </li>
    <li>
        普通のimgタグ こっちでも動的に画像を表示可能(src属性をプロパティバインディングしている)
        <img [src]="logoUrl" [alt]="logoAlt" width="32" height="32" />
    </li>
    </ul>
    <hr/>
    <ul>
      <li>
        静的画像 Static Image: ngSrc属性の値がファイルパスで固定されている場合
        <img ngSrc="/assets/logo.svg" alt="Angular ロゴ" width="32" height="32" />
      </li>
      <li>
        
        動的画像 Dynamic Image: ngSrc属性の値=ファイルパスが、コンポーネントのプロパティから取得される場合<br/>
        ngSrc属性をプロパティバインディングしている<br/>
        <img [ngSrc]="logoUrl" [alt]="logoAlt" width="32" height="32" />
      </li>
    </ul>
  `,
  // 画像最適化のため↑でimportしたNgOptimizedImageを使うためimportsに追加
  imports: [NgOptimizedImage],
})
export class User {
  logoUrl = '/assets/logo.svg';
  logoAlt = 'Angular logo';
  username = 'youngTech';
}