
import random
class Car:
    def __init__(self, reg_number, max_speed):
        self.reg_number = reg_number
        self.max_speed = max_speed
        self.current_speed = 0
        self.distance_traveled = 0

    def accelerate(self, change):
        self.current_speed += change
        if self.current_speed > self.max_speed:
            self.current_speed = self.max_speed
        if self.current_speed < 0:
            self.current_speed = 0

    def drive(self, hours):
        self.distance_traveled += self.current_speed * hours


class Race:
    def __init__(self, name, distance, cars):
        self.name = name
        self.distance = distance
        self.cars = cars

    def hour_passes(self):
        for car in self.cars:
            change = random.randint(-10, 15)
            car.accelerate(change)
            car.drive(1)

    def print_status(self):
        print(f"\nRace: {self.name}")
        print(f"{'Car':<10}{'Speed':<10}{'Distance':<15}")
        for car in self.cars:
            print(f"{car.reg_number:<10}{car.current_speed:<10}{car.distance_traveled:<15.2f}")

    def race_finished(self):
        return any(car.distance_traveled >= self.distance for car in self.cars)


if __name__ == "__main__":
    cars = []
    for i in range(10):
        reg = f"ABC-{i+1}"
        max_speed = random.randint(100, 200)
        cars.append(Car(reg, max_speed))

    race = Race("Grand Demolition Derby", 8000, cars)

    hours = 0
    while not race.race_finished():
        race.hour_passes()
        hours += 1
        if hours % 10 == 0:
            race.print_status()

    race.print_status()