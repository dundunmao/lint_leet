# enum type for Vehicle
import logging


class VehicleSize:
    Motorcycle = 1
    Compact = 2
    Large = 3
    Other = 99

class Vehicle(object):
    # Write your code here
    def __init__(self):
        self.size = 0
        self.vid = None
        self.spots_needed = 0


class Motorcycle(Vehicle):
    def __init__(self):
        super(Motorcycle,self).__init__()
        self.size = VehicleSize.Motorcycle
        self.spots_needed = 1

    def can_fit_in_spot(self, spot):
        return True


class Car(Vehicle):
    def __init__(self):
        super(Car,self).__init__()
        self.size = VehicleSize.Compact
        self.spots_needed = 1

    def can_fit_in_spot(self, spot):
        return spot.get_size() == VehicleSize.Large or spot.get_size() == VehicleSize.Compact


class Bus(Vehicle):
    def __init__(self):
        super(Bus, self).__init__()
        self.size = VehicleSize.Compact
        self.spots_needed = 5

    def can_fit_in_spot(self, spot):   #spot = ParkingSpot()
        return spot.get_size() == VehicleSize.Large

class ParkingSpot:
    # Write your code here
    def __init__(self, lvl, r, n, sz):
        self.level = lvl
        self.row = r
        self.spot_number = n
        self.spot_size = sz
        self.vehicle = None

    def is_available(self):
        return self.vehicle == None

    def can_fit_vehicle(self, vehicle):   #vehicle = Motorcycle() or Car() or Bus()
        return self.is_available() and vehicle.can_fit_in_spot(self)

    def park(self, v):
        if not self.can_fit_vehicle(v):
            return False

        self.vehicle = v       #v = Motorcycle() or Car() or Bus()
        self.vehicle.park_in_spot(self)
        return True

    def remove_vehicle(self):
        self.level.spot_freed()
        self.vehicle = None

    def get_row(self):
        return self.row

    def get_spot_number(self):
        return self.spot_number

    def get_size(self):
        return self.spot_size

class Level:
    def __init__(self, level):
        self.level = level


class ParkingLot:
    def __init__(self, n, num_rows, spots_per_row):
        self.l = n
        self.r = num_rows
        self.c = spots_per_row
        w, h = 8, 5.
        self.spots=[[0 for x in range(w)] for y in range(h)]


        # Park the vehicle in a spot (or multiple spots)
    # Return false if failed
    def park_vehicle(self, vehicle):


        return False
        # Write your code here


    # unPark the vehicle
    def unpark_vehicle(self, vehicle):
        # Write your code here
        return

