// app.tsでcar.service.tsを使うための、抽象クラスとInjectionTokenの定義
import { InjectionToken } from '@angular/core';

export interface AbstractCarService {
  getCars(): string[];
  getCar(id: number): string;
}

export const ABSTRACT_CAR_SERVICE = new InjectionToken<AbstractCarService>('ABSTRACT_CAR_SERVICE');