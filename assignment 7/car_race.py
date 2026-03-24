import random

class Car:
    def __init__(self, registration_number, max_speed):
        self.registration_number = registration_number
        self.max_speed = max_speed
        self.current_speed = 0
        self.travelled_distance = 0

    def accelerate(self, change):
        self.current_speed += change
        if self.current_speed > self.max_speed:
            self.current_speed = self.max_speed
        if self.current_speed < 0:
            self.current_speed = 0

    def drive(self, hours):
        self.travelled_distance += self.current_speed * hours
cars = []
for i in range(10):
    reg = f"ABC-{i+1}"
    max_speed = random.randint(150, 200)
    cars.append(Car(reg, max_speed))


race_finished = False

while not race_finished:
    for car in cars:
        change = random.randint(-10, 15)
        car.accelerate(change)
        car.drive(1)

        if car.travelled_distance >= 10000:
            race_finished = True

print(f"{'Reg':<10} {'Max':<10} {'Speed':<10} {'Distance':<10}")
for car in cars:
    print(f"{car.registration_number:<10} {car.max_speed:<10} {car.current_speed:<10} {int(car.travelled_distance):<10}")