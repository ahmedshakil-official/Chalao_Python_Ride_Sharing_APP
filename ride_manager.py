class RideManager:
    def __init__(self):
        self.__available_cars = []
        self.__available_bikes = []
        self.__available_cngs = []

    def add_a_vehicle(self, vehicle_type, vehicle):
        if vehicle_type == 'car':
            self.__available_cars.append(vehicle)
        elif vehicle_type == 'bike':
            self.__available_bikes.append(vehicle)
        elif vehicle_type == 'cng':
            self.__available_cngs.append(vehicle)

    def get_available_car(self):
        return self.__available_cars

    def find_a_vehicle(self, rider, vehicle_type, destination):
        if vehicle_type != 'car':
            return
        if len(self.__available_cars) == 0:
            print('No cars are available')
            return False
        for car in self.__available_cars:
            if car.status == 'available' and abs(rider.location - car.driver.location) <= 30:
                distance = abs(rider.location - destination)
                fare = distance * car.rate
                print(f"Find a match for you and fare is {fare}.")
                confirmation = input("Are you want to confirm ride? ")
                if confirmation.lower() == 'yes':
                    car.status = 'unavailable'
                    rider.accept_ride(fare)
                else:
                    rider.cancel_trip()


uber = RideManager()
