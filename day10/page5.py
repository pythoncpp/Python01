# has-a
# composition


class Engine:

    def __init__(self, engine_type, engine_details):
        self.__engine_type = engine_type
        self.__engine_details = engine_details

    def print_details(self):
        print('engine_type: ', self.__engine_type)
        print('engine_details: ', self.__engine_details)


class Bike:

    def __init__(self, engine_type, engine_details, model):
        self.__model = model
        self.__engine = Engine(engine_type, engine_details)

    def print_details(self):
        print('model: ', self.__model)
        self.__engine.print_details()


bike1 = Bike('engine 2', 'details', 'shine')
bike1.print_details()


class Rocket:

    def __init__(self, engine_type, engine_details, company):
        # self.__engine_type = engine_type
        # self.__engine_details = engine_details
        self.__engine = Engine(engine_type, engine_details)
        self.__company = company

    def print_details(self):
        # print('engine_type: ', self.__engine_type)
        # print('engine_details: ', self.__engine_details)
        print('company: ', self.__company)
        self.__engine.print_details()



rocket = Rocket('engine 1', 'details', 'ISRO')
rocket.print_details()


class Car:

    def __init__(self, engine_type, engine_details, model, company):
        # self.__engine_type = engine_type
        # self.__engine_details = engine_details
        self.__engine = Engine(engine_type, engine_details)
        self.__model = model
        self.__company = company

    def print_details(self):
        # print('engine_type: ', self.__engine_type)
        # print('engine_details: ', self.__engine_details)
        print('model: ', self.__model)
        print('company: ', self.__company)
        self.__engine.print_details()


car = Car('v1', 'nice engine', 'nano', 'tata')
car.print_details()
