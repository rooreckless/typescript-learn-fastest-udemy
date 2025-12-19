// import { Component, signal } from '@angular/core';
// import { RouterOutlet } from '@angular/router';

// @Component({
//   selector: 'app-root',
//   imports: [RouterOutlet],
//   templateUrl: './app.html',
//   styleUrl: './app.css'
// })
// export class App {
//   protected readonly title = signal('project_angular_01');
// }

import {Component,Inject} from '@angular/core';
import {CarService,FakeCarService} from './car.service';
import {ABSTRACT_CAR_SERVICE,AbstractCarService} from './abstract.car.service';

@Component({
  selector: 'app-root',
  template: `
    
    <p>car.getCars() : {{car.getCars()}}</p>
  `,
  // DIPのために、providers配列でCarServiceを登録
  //これは、抽象クラスと、実装クラスのひもづけを行う部分でもある
  providers: [
    // { provide: ABSTRACT_CAR_SERVICE, useClass: CarService }
    // DI/DIPが成り立っているので、provicers配列で
    //AbstractCarServiceに紐づける実装クラスを変更するだけで
    //コンポーネント側のコードを一切変更せずに、サービスの入れ替えが可能
    { provide: ABSTRACT_CAR_SERVICE, useClass: FakeCarService }
  ],
imports: [],
})
export class App {
  // car = new CarService();
  //↑サービスを直接newして使うのはNG。DIPに反する。

  // コンストラクタで抽象クラスを使って依存性注入を行う
  constructor(
    @Inject(ABSTRACT_CAR_SERVICE)
    public car: AbstractCarService
  ) {
    // コンストラクタとしてやる処理はない。↑のAbstractな引数だけで十分
    //これで、テンプレートでcar.getCars()をすると、provides配列で登録した
    //CarServiceのメソッドが呼び出される。
  }
}