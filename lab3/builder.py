class House:
    def __init__(self):
        self.parts = []

    def show(self):
        return "+".join(self.parts)


class HouseBuilder:
    def __init__(self):
        self.house = House()

    def walls(self):
        self.house.parts.append("Walls")
        return self

    def roof(self):
        self.house.parts.append("Roof")
        return self

    def door(self):
        self.house.parts.append("Door")
        return self

    def build(self):
        result = self.house
        self.house = House()
        return result


if __name__ == "__main__":
    house = HouseBuilder().walls().door().roof().build()
    print("Builder:", house.show())

