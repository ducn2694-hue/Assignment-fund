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


car = Car("ABC-123", 142)

car.accelerate(30)
car.accelerate(70)
car.accelerate(50)

print("Current speed:", car.current_speed)

car.accelerate(-200)

print("Final speed:", car.current_speed)