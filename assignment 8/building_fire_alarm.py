
class Elevator:
    def __init__(self, bottom, top):
        self.bottom = bottom
        self.top = top
        self.current_floor = bottom
        print(f"Start at floor {self.current_floor}")

    def floor_up(self):
        if self.current_floor < self.top:
            self.current_floor += 1
            print(f"Floor {self.current_floor}")

    def floor_down(self):
        if self.current_floor > self.bottom:
            self.current_floor -= 1
            print(f"Floor {self.current_floor}")

    def go_to_floor(self, target_floor):
        print(f"Going to floor {target_floor}")
        while self.current_floor < target_floor:
            self.floor_up()
        while self.current_floor > target_floor:
            self.floor_down()
        print(f"Arrived at floor {self.current_floor}")


class Building:
    def __init__(self, bottom, top, num_elevators):
        self.bottom = bottom
        self.top = top
        self.elevators = [Elevator(bottom, top) for _ in range(num_elevators)]

    def run_elevator(self, elevator_number, destination_floor):
        print(f"\nRunning elevator {elevator_number} to floor {destination_floor}")
        self.elevators[elevator_number].go_to_floor(destination_floor)

    def fire_alarm(self):
        print("\nFIRE ALARM! Moving all elevators to bottom floor...")
        for i, elevator in enumerate(self.elevators):
            print(f"Elevator {i} going to bottom floor")
            elevator.go_to_floor(self.bottom)


if __name__ == "__main__":
    b = Building(1, 10, 3)
    b.run_elevator(0, 5)
    b.run_elevator(1, 7)
    b.run_elevator(2, 9)
    b.fire_alarm()