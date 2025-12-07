import {Component, output} from '@angular/core';

@Component({
    selector: 'app-child',
    styles: `.btn { padding: 5px; }`,
    template: `
        <button class="btn" (click)="addItem()">Add Item</button>
    `,
})
export class Child {
    // 出力プロパティ(stringを送信)を定義 = 親コンポーネントへ通知するため
    addItemEvent = output<string>();
    // ボタンがクリックされたときに呼び出されるメソッド
    addItem() {
        // やることは、addItemEventを発火させて、文字列'🐢'を送信すること
        this.addItemEvent.emit('🐢');
    }
}
