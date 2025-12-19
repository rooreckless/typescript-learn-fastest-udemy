export class Car {
    cars = ['Sunflower GT', 'Flexus Sport', 'Sprout Mach One'];

    getCars(): string[] {
        return this.cars;
    }

    getCar(id: number) {
        return this.cars[id];
    }
}