// このapp.routes.tsファイルは、Angularアプリケーションのルーティング情報を定義するためのものです。
// ここでは、Routes型の空の配列をエクスポートしています。
// 将来的にルーティング情報を追加する際の基礎として機能します。
import { Routes } from '@angular/router';
// 例えば、このファイルと同階層のhomeディレクトリのHomeコンポーネントや,
// 同階層のuserディレクトリのUserコンポーネントなどのルートを追加する場合は、以下のように記述します。
import {Home} from './home/home';
import {User} from './user/user';

export const routes: Routes = [
    // ↑でインポートしたHomeコンポーネントとUserコンポーネントを使ってルートを定義
    {
        path: '',
        component: Home,
    },
    {
        path: 'user',
        component: User,
    },
];
