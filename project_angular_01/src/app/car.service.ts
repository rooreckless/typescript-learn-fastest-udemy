import { Injectable } from "@angular/core";
import { AbstractCarService } from "./abstract.car.service";

// AbstractCarServiceを実装したCarServiceクラスの定義
// @Injectableデコレーターを使用して、依存性注入が可能なサービスとして定義

// @Injectable({ providedIn: 'root'}) // でもOKだが、今回はあえて、app.tsのコンポーネントでproviders配列で登録する方法を使う
@Injectable()
export class CarService implements AbstractCarService {
    cars = ['Sunflower GT', 'Flexus Sport', 'Sprout Mach One'];

    getCars(): string[] {
        return this.cars;
    }

    getCar(id: number) {
        return this.cars[id];
    }
}

