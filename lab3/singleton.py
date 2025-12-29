class Singleton:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.value = 0
        return cls._instance

    def increment(self):
        self.value += 1
        print(self.value)


if __name__ == "__main__":
    s1 = Singleton()
    s1.increment()

    s2 = Singleton()
    s2.increment()

    print(s1 is s2)

