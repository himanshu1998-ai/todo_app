from typing import Union, List
from todo.repository.interfaces.todo_repo import ITodoREPO
from todo.schemas.schemas import TODOSchema
from common.exception import not_found


class TodoStore(ITodoREPO):

    def __init__(self, db_name: str, collection_name: str):
        super().__init__(db_name=db_name, collection_name=collection_name)

    async def create_todo(self, todo: TODOSchema) -> str:
        document = todo.model_dump()
        document["_id"] = document.pop("id")
        try:
            data = await self._collection.insert_one(document)
            if data:
                return f"Insert success with data: {document}"
        except Exception as e:
            return f"Exception: {e} occurred while creating todo with data: {document}"

    async def fetch_one_todo(self, todo_id: int) -> Union[TODOSchema, str]:
        try:
            data = await self._collection.find_one({"_id": todo_id})
            if not data:
                return not_found(detail=f"todo with the id {todo_id} is not available")
            data["id"] = data.pop('_id')
            return TODOSchema(**data)
        except Exception as e:
            return f"Exception: {e} occurred while fetching todo with todo_id: {todo_id}"

    async def fetch_all_todo(self) -> Union[List[TODOSchema], str]:
        try:
            data = self._collection.find({})
            todos = []
            async for todo in data:
                todo["id"] = todo.pop('_id')
                todos.append(TODOSchema(**todo))
            return todos
        except Exception as e:
            return f"Exception: {e} occurred while fetching all todos"

    async def update_todo(self, todo: dict) -> str:
        try:
            todo_id = todo.pop('id')
            _todo = await self._collection.find_one({"_id": todo_id})
            if _todo:
                await self._collection.update_one({"_id": todo_id}, {"$set": todo})
                return f"update success with data: {todo}"
            return not_found(detail=f"todo with the id {todo_id} is not valid")
        except Exception as e:
            return f"Exception: {e} occurred while updating todo"

    async def delete_todo(self, todo_id: int) -> Union[int, str]:
        try:
            todo = await self._collection.find_one({"_id": todo_id})
            if todo:
                await self._collection.delete_one({"_id": todo_id})
                return f"deleted todo with id: {todo_id}"
            return not_found(detail=f"todo with the id {todo_id} is not valid")
        except Exception as e:
            return f"Exception: {e} occurred while deleting todo"

