// CarServiceクラスを、newを使わなくても使えるようにするためIngetcatbleデコレータを使う
// (注入される側=サービス側はこれだけでいい)
import {Injectable} from '@angular/core';

@Injectable({ providedIn: 'root'})
export class CarService {
  cars = ['Sunflower GT', 'Flexus Sport', 'Sprout Mach One'];

  getCars(): string[] {
    return this.cars;
  }

  getCar(id: number) {
    return this.cars[id];
  }
}
