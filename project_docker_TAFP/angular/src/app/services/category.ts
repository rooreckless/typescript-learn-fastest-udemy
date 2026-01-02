import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';

@Injectable({
  providedIn: 'root',
})
export class CategoryService {
    private readonly API = 'http://localhost/api';
    constructor(private http: HttpClient) { // HttpClientをコンストラクタで注入
    }
    getCategories() {
        return this.http.get(`${this.API}/categories`);
        // return this.http.get('http://localhost/api/categories', {responseType: 'json'});
    }

    createCategory(data: any) {
        return this.http.post(`${this.API}/categories`, data);
    }
}
