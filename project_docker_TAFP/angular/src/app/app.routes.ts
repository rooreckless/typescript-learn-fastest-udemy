/**
 * =========================================
 * ルーティング設定
 * =========================================
 */

import { Routes } from '@angular/router';
import { Home } from './home/home';
import { RecipeList } from './recipe-list/recipe-list';
import { RecipeDetail } from './recipe-detail/recipe-detail';
import { RecipeForm } from './recipe-form/recipe-form';

export const routes: Routes = [
  // ここにルートを追加
  // 例: { path: 'users', component: UsersComponent }
  { path: '', component: Home },
  { path: 'recipes', component: RecipeList },
  { path: 'recipe/new', component: RecipeForm },  // 新規作成用ルート（動的ルートより前に配置）
  { path: 'recipes/:id', component: RecipeDetail },  // 動的ルート
  { path: '**', redirectTo: '' }
];
