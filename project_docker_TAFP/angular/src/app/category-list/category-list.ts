import { Component,inject,signal } from '@angular/core';
import { CategoryService } from '../services/category';
@Component({
  selector: 'app-category-list',
  imports: [],
  templateUrl: './category-list.html',
  styleUrl: './category-list.css',
})
export class CategoryList {
  private categoryService = inject(CategoryService);
  categories = signal<any[]>([]);
  
  constructor() {
    this.categoryService.getCategories().subscribe((data: any) => {
      console.log(data);
      console.log(typeof data);
      console.log(Array.isArray(data));
      console.log(data.length);
      console.log(data[0]);
      this.categories.set(data);
    });
  }
}
