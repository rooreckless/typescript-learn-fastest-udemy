/**
 * =========================================
 * ルーティング設定
 * =========================================
 */

import { Routes } from '@angular/router';
import { Home } from './home/home';
import { RecipeList } from './recipe-list/recipe-list';
import { RecipeDetail } from './recipe-detail/recipe-detail';

export const routes: Routes = [
  // ここにルートを追加
  // 例: { path: 'users', component: UsersComponent }
  { path: '', component: Home },
  { path: 'recipes', component: RecipeList },
  { path: 'recipes/:id', component: RecipeDetail },  // 動的ルート追加
  { path: '**', redirectTo: '' }
];
