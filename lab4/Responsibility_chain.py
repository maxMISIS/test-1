from __future__ import annotations
from dataclasses import dataclass
from typing import Optional


# Запрос, проходящий по цепочке
@dataclass(frozen=True)
class Request:
    user: str
    amount: int
    country: str
    is_vip: bool = False


# Базовый обработчик
class Handler:
    def __init__(self, next_handler: Optional["Handler"] = None) -> None:
        self._next = next_handler

    def handle(self, req: Request) -> str:
        if self._next is None:
            return "APPROVED"
        return self._next.handle(req)


# Проверка пользователя
class AuthHandler(Handler):
    def handle(self, req: Request) -> str:
        if not req.user:
            return "REJECTED: no user"
        return super().handle(req)


# Проверка суммы
class AmountHandler(Handler):
    def __init__(self, limit: int, next_handler: Optional[Handler] = None) -> None:
        super().__init__(next_handler)
        self._limit = limit

    def handle(self, req: Request) -> str:
        if req.amount > self._limit and not req.is_vip:
            return "REJECTED: limit exceeded"
        return super().handle(req)


# Проверка страны
class CountryHandler(Handler):
    def __init__(self, banned: set[str], next_handler: Optional[Handler] = None) -> None:
        super().__init__(next_handler)
        self._banned = banned

    def handle(self, req: Request) -> str:
        if req.country in self._banned:
            return "REJECTED: banned country"
        return super().handle(req)


# Пример 
if __name__ == "__main__":
    chain = AuthHandler(
        AmountHandler(
            1000,
            CountryHandler({"IR", "NK"})
        )
    )

    print(chain.handle(Request("Maxim", 500, "DE")))
    print(chain.handle(Request("", 100, "DE")))
    print(chain.handle(Request("Maxim", 5000, "DE")))
    print(chain.handle(Request("Maxim", 5000, "DE", is_vip=True)))
    print(chain.handle(Request("Maxim", 100, "IR")))
