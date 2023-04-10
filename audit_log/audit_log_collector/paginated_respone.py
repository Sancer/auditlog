from dataclasses import dataclass
from typing import TypeVar, Generic


T = TypeVar("T")


@dataclass
class PaginatedResponse(Generic[T]):
    count: int
    results: list[T]

    def dict(self):
        return {"count": self.count, "results": [item.dict() for item in self.results]}
