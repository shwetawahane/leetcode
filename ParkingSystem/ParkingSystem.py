class ParkingSystem:

    def __init__(self, big: int, medium: int, small: int):
        self.big = big
        self.medium = medium
        self.small = small
        self.map = {1:self.big, 2: self.medium, 3: self.small}

    def addCar(self, carType: int) -> bool:
        
        if self.map[carType] > 0:
            self.map[carType] = self.map[carType] - 1
            return True
        else:
            return False



# Your ParkingSystem object will be instantiated and called as such:
#obj = ParkingSystem(big, medium, small)
#param_1 = obj.addCar(carType)
