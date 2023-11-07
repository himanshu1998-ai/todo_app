from typing import Union

from todo.repository.interfaces.todo_repo import ITodoREPO
from todo.schemas.schemas import TODOSchema


class UpdateTodoUsecase:
    def __init__(self, repo: ITodoREPO):
        self._repo = repo

    async def execute(self, todo_id: int, todo: TODOSchema) -> Union[TODOSchema, str]:
        data = await self._repo.update_todo(todo_id=todo_id, todo=todo)
        return data
