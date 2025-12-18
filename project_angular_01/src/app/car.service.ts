

// CarServiceクラスを、newを使わなくても使えるようにするためIngetcatbleデコレータを使う
// (注入される側=サービス側はこれだけでいい)
import {Injectable} from '@angular/core';
// 抽象クラスをimplementsして型を合わせる(=依存性逆転のため、サービス側が守らなければならない実装ルールをインポート)
import {AbstractCartService} from './abstract.car.service';

@Injectable({ providedIn: 'root'})
export class CarService implements AbstractCartService {
  cars = ['Sunflower GT', 'Flexus Sport', 'Sprout Mach One'];

  getCars(): string[] {
    return this.cars;
  }

  getCar(id: number) {
    return this.cars[id];
  }
}
