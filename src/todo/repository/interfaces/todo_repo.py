from typing import List
from abc import ABC, abstractmethod
from todo.entity.todo_entity import TODO
from todo.schemas.schemas import TODOSchema
from common.utils import get_db


class ITodoREPO(ABC):
    def __init__(self, db_name: str, collection_name: str):
        self._client = get_db()
        self._database = self._client[db_name]
        self._collection = self._database[collection_name]

    @abstractmethod
    async def create_todo(self, todo_id: int, todo: TODOSchema) -> str:
        pass

    @abstractmethod
    async def fetch_one_todo(self, todo_id: int) -> TODOSchema:
        pass

    @abstractmethod
    async def delete_todo(self, todo_id: int) -> int:
        pass

    @abstractmethod
    async def fetch_all_todo(self) -> List[TODOSchema]:
        pass

    @abstractmethod
    async def update_todo(self, todo_id: int, todo: TODOSchema) -> str:
        pass

