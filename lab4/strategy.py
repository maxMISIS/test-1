from dataclasses import dataclass
from typing import Protocol


# Интерфейс стратегии
class PricingStrategy(Protocol):
    def price(self, base: float) -> float: ...


# Обычная цена без скидки
class RegularPrice:
    def price(self, base: float) -> float:
        return base


# Процентная скидка
class PercentDiscount:
    def __init__(self, percent: float) -> None:
        self._k = 1.0 - percent / 100.0

    def price(self, base: float) -> float:
        return base * self._k


# Фиксированная скидка
class FixedDiscount:
    def __init__(self, amount: float) -> None:
        self._amount = amount

    def price(self, base: float) -> float:
        return max(0.0, base - self._amount)


# Контекст, использующий стратегию
@dataclass
class Order:
    base_total: float
    strategy: PricingStrategy

    def total(self) -> float:
        return self.strategy.price(self.base_total)


# Пример 
if __name__ == "__main__":
    order = Order(1000.0, RegularPrice())
    print(order.total())

    order.strategy = PercentDiscount(10)
    print(order.total())

    order.strategy = FixedDiscount(300)
    print(order.total())
