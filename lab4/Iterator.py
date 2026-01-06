from dataclasses import dataclass
from typing import Iterable, Iterator, List


# Элемент коллекции
@dataclass(frozen=True)
class Task:
    name: str
    priority: int


# Коллекция с собственным итератором
class TaskBoard(Iterable[Task]):
    def __init__(self) -> None:
        self._tasks: List[Task] = []

    def add(self, task: Task) -> None:
        self._tasks.append(task)

    #сортировка по приоритету
    def __iter__(self) -> Iterator[Task]:
        return iter(sorted(self._tasks, key=lambda t: -t.priority))


# Пример 
if __name__ == "__main__":
    board = TaskBoard()
    board.add(Task("Write report", 2))
    board.add(Task("Fix bug", 5))
    board.add(Task("Deploy", 4))

    for task in board:
        print(task)
