class Transport:
    def move(self):
        raise NotImplementedError


class Car(Transport):
    def move(self):
        return "Car"


class Bike(Transport):
    def move(self):
        return "Bike"


class TransportFactory:
    def create(self):
        raise NotImplementedError


class CarFactory(TransportFactory):
    def create(self):
        return Car()


class BikeFactory(TransportFactory):
    def create(self):
        return Bike()


if __name__ == "__main__":
    print("Factory Method:", CarFactory().create().move(), BikeFactory().create().move())
