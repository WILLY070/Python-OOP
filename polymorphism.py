class Car:
    def __init__(self,action):
        self.action = action
    def move(self):
        return f"The car is {self.action}"
class Bike:
    def __init__(self,action):
        self.action = action
    def move(self):
        return f"The bike is {self.action}"
    
my_car = Car("driving")
my_bike = Bike("cycling")
print(my_car.move())
print(my_bike.move())