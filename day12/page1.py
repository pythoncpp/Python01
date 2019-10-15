class Vehicle:

    def __init__(self, engine, company):
        self._engine = engine
        self._company = company

    def print_vehicle_details(self):
        print('engine: ', self._engine)
        print('company: ', self._company)


class Car(Vehicle):

    def __init__(self, engine, company, model):
        Vehicle.__init__(self, engine, company)
        self._model = model

    def print_car_details(self):
        Vehicle.print_vehicle_details(self)
        print('model: ', self._model)


class Bike(Vehicle):

    def __init__(self, engine, company, model):
        # Vehicle.__init__(self, engine, company)
        super().__init__(engine, company)
        self._model = model

    def print_bike_details(self):
        # Vehicle.print_vehicle_details(self)
        super().print_vehicle_details()
        print('model: ', self._model)


# car = Car('v2.0', 'company 1', 'model 1')
# car.print_vehicle_details()
# car.print_car_details()

bike = Bike('v1.0', 'company 2', 'model 2')
# bike.print_vehicle_details()
bike.print_bike_details()
