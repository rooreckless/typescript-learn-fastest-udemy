import { Component } from '@angular/core';
import { RouterLink } from '@angular/router';
@Component({
  selector: 'app-home',
  // ルーターによって、<router-outlet> タグに差し込まれるために、imports 配列に RouterLink を追加します
  imports: [RouterLink],
  templateUrl: './home.html',
  styleUrl: './home.css',
})
export class Home {

}
