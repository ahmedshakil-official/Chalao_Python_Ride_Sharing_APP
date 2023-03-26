from abc import ABC, abstractmethod


class Vehicle(ABC):

    speeds = {
        'car': 30,
        'bike': 50,
        'cng': 15
    }

    def __init__(self, vehicle_type, license_plate, rate, driver):
        self.vehicle_type = vehicle_type
        self.rate = rate
        self.driver = driver
        self.speed = self.speeds[vehicle_type]
        self.license_plate = license_plate
        self.status = 'available'
        self.balance = 0

    @abstractmethod
    def start_driving(self):
        pass

    @abstractmethod
    def trip_finished(self):
        pass

    def add_earnings(self, balance):
        self.balance += balance


class Car(Vehicle):

    def __init__(self, vehicle_type, license_plate, rate, driver):
        super().__init__(vehicle_type, license_plate, rate, driver)

    def start_driving(self):
        self.status = 'unavailable'
        print(f'{self.vehicle_type} is started. License no {self.license_plate}')

    def trip_finished(self):
        self.status = 'available'
        print(f'{self.vehicle_type} with license no {self.license_plate} completed trip!')


class Bike(Vehicle):

    def __init__(self, vehicle_type, license_plate, rate, driver):
        super().__init__(vehicle_type, license_plate, rate, driver)

    def start_driving(self):
        self.status = 'unavailable'
        print(f'{self.vehicle_type} is started. License no {self.license_plate}')

    def trip_finished(self):
        self.status = 'available'
        print(f'{self.vehicle_type} with license no {self.license_plate} completed trip!')


class Cng(Vehicle):

    def __init__(self, vehicle_type, license_plate, rate, driver):
        super().__init__(vehicle_type, license_plate, rate, driver)

    def start_driving(self):
        self.status = 'unavailable'
        print(f'{self.vehicle_type} is started. License no {self.license_plate}')

    def trip_finished(self):
        self.status = 'available'
        print(f'{self.vehicle_type} with license no {self.license_plate} completed trip!')
