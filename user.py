import hashlib
import random

from authority import BRTA
from vehicales import Car, Bike, Cng
from ride_manager import uber

license_authority = BRTA()


class UserAlreadyExistException(Exception):
    def __init__(self, email):
        print(f'User {email} already exist!')


class User:
    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        enc_pass = hashlib.md5(password.encode()).hexdigest()
        already_exist = False
        with open('users.txt', 'r') as file:
            if email in file.read():
                already_exist = True
                print(f'User {email} already exist!')
        file.close()
        if not already_exist:
            with open('users.txt', 'a') as file:
                file.write(f'{email} {enc_pass}\n')
                print(self.name, "user created")
        file.close()

    @staticmethod
    def log_in(email, password):
        user_pass = ''
        with open('users.txt', 'r') as f:
            users = f.readlines()
            for user in users:
                user_email, user_pass = user.split(' ')

        f.close()
        new_enc_pass = hashlib.md5(password.encode()).hexdigest()
        if user_email == email and user_pass == new_enc_pass:
            print("Login Successful!")
        else:
            print("Invalid User!")


class Rider(User):

    def __init__(self, name, email, password, location, balance):
        super().__init__(name, email, password)
        self.location = location
        self.balance = balance
        self.accept = False

    def set_location(self, location):
        self.location = location

    def get_location(self):
        return self.location

    def request_trip(self, destination):
        pass

    def start_trip(self, fare):
        self.balance -= fare


    def accept_ride(self, fare):
        self.accept = True
        if self.balance < fare:
            print("You have not enough money!")
            return
        self.start_trip(fare)
        print(f'Have a nice trip\nYour fare is {fare}')
        return

    def cancel_trip(self):
        self.accept = False
        print('Trip canceled!')
        return


class Driver(User):

    def __init__(self, name, email, password, location, license):
        super().__init__(name, email, password)
        self.location = location
        self.valid_driving_test = license_authority.driving_test(email)
        self.valid_driver = license_authority.validate_license(email, license)
        if self.valid_driver and self.valid_driving_test:
            self.license = license
        else:
            self.license = False
        self.earning = 0

    def register_a_vehicle(self, vehicle_type, license_plate, rate):

        if self.valid_driver:
            new_vehicle = None
            if vehicle_type == 'car':
                new_vehicle = Car(vehicle_type, license_plate, rate, self)
            elif vehicle_type == 'bike':
                new_vehicle = Bike(vehicle_type, license_plate, rate, self)
            elif vehicle_type == 'cng':
                new_vehicle = Cng(vehicle_type, license_plate, rate, self)
            uber.add_a_vehicle(vehicle_type, new_vehicle)
            # print(new_vehicle)

    def start_trip(self, fare, destination):
        self.earning += fare
        self.location = destination


rider1 = Rider('rider1', 'r1@gmail.com', '1234', random.randint(0, 50), 520)
rider2 = Rider('rider2', 'r2@gmail.com', '1230', random.randint(0, 50), 620)
rider3 = Rider('rider3', 'r3@gmail.com', '1239', random.randint(0, 40), 320)

driver1 = Driver('driver1', 'd1@gmail.com', '2222', random.randint(0, 70), 5342)
driver2 = Driver('driver2', 'd2@gmail.com', '3333', random.randint(0, 66), 5344)
driver3 = Driver('driver3', 'd3@gmail.com', '4444', random.randint(0, 77), 5345)
driver4 = Driver('driver4', 'd4@gmail.com', '5555', random.randint(0, 33), 5346)
driver1.register_a_vehicle('car', 5342, 15)
driver2.register_a_vehicle('cng', 5343, 10)
driver3.register_a_vehicle('bike', 5344, 12)
driver4.register_a_vehicle('car', 5345, 15)
uber.find_a_vehicle(rider1, 'car', 88)
