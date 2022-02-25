class ParkingSystem:
    def __init__(self, big: int, medium: int, small: int):
        self.big = big
        self.medium = medium
        self.small = small

    def addCar(self, carType: int):
        if carType == 1:
            self.big = self.big - 1
            if self.big < 0:
                return False
            else:   return True
        elif carType == 2:
            self.medium = self.medium - 1
            if self.medium < 0:
                return False
            else:   return True
        elif carType == 3:
            self.small = self.small - 1
            if self.small < 0:
                return False
            else:   return True
        else:   return null
