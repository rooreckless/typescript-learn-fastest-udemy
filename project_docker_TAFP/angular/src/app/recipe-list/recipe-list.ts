import { Component, signal, computed, inject } from '@angular/core';
// 双方向バインディングのためにインポート
import { FormsModule } from '@angular/forms';
// ルーティングのためにインポート
import { RouterLink } from '@angular/router';
import { RecipeService } from '../services/recipe';
import { RecipeModel } from '../models';
// @angular/materialをinstallしたのでインポートする
import { MatCardModule } from '@angular/material/card';


@Component({
  selector: 'app-recipe-list',
  imports: [FormsModule, RouterLink, MatCardModule],  // RecipeDetailを削除、RouterLinkを追加
  templateUrl: './recipe-list.html',
  styleUrls: ['./recipe-list.css'],
})
export class RecipeList {
  private recipeService = inject(RecipeService);
  
  // 全レシピを取得
  protected readonly recipes = signal<RecipeModel[]>(this.recipeService.getAllRecipes());
  
  // Module 13: Two-Way Binding (双方向バインディング)
  // 検索用の文字列格納signal
  protected readonly search_text_for_recipe = signal<string>('');
  
  // フィルタリングされたレシピリスト
  protected readonly filteredRecipes = computed(() => {
    const searchText = this.search_text_for_recipe();
    if (!searchText) {
      // 検索文字列が空の場合は全レシピを返す
      return this.recipes();
    }
    // 検索文字列がある場合はフィルタリング
    return this.recipeService.searchRecipes(searchText);
  });
}
