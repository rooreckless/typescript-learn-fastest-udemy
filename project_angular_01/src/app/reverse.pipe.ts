//カスタムパイプを定義するためのソース・ファイル
import {Pipe, PipeTransform} from '@angular/core';

// 逆順にするカスタムパイプ
// (カスタムパイプ定義には@PipeデコレーターとPipeTransformインターフェースを使う)
@Pipe({
  //パイプ名を'reverse'に設定。つまりテンプレートでは{{ 変数 | reverse }}のように使う
  name: 'reverse'
})
export class ReversePipe implements PipeTransform {
    // reverseパイプの変換ロジックはここで実装する。
    // PipeTransformインターフェースのtransformメソッドを実装
    transform(value: string): string {
        return value.split('').reverse().join('');
    }
}