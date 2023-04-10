from abc import ABC, abstractmethod
from dataclasses import dataclass
from datetime import datetime

from .paginated_respone import PaginatedResponse


@dataclass
class Log:
    instance_type: str
    instance_id: int
    previous_state: dict
    actual_state: dict
    author: str
    created: datetime

    def dict(self):
        return self.__dict__


class AuditLogRepository(ABC):
    @abstractmethod
    def save(self, log: Log) -> None:
        raise NotImplementedError

    @abstractmethod
    def search(
        self,
        instance_type: str = None,
        instance_id: int = None,
        created_from: str = None,
        created_to: str = None,
        author: str = None,
        limit: int = None,
        offset: int = None,
    ) -> PaginatedResponse[Log]:
        raise NotImplementedError
