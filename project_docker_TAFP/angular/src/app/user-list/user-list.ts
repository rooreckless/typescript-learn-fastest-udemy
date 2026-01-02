import { Component,inject,signal } from '@angular/core';
import { UserService } from '../services/user';


@Component({
  selector: 'app-user-list',
  imports: [],
  templateUrl: './user-list.html',
  styleUrl: './user-list.css',
})
export class UserList {
  private userService = inject(UserService);
  users = signal<any[]>([]);

  constructor() {
    this.userService.getUsers().subscribe((data: any) => {
      console.log(data);
      console.log(typeof data);
      console.log(Array.isArray(data));
      console.log(data.length);
      console.log(data[0]);
      this.users.set(data);
    });
  }
}







