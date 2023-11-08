from typing import Union

from todo.repository.interfaces.todo_repo import ITodoREPO
from todo.schemas.schemas import TODOSchema


class FetchOneTodoUsecase:
    def __init__(self, repo: ITodoREPO):
        self._repo = repo

    async def execute(self, todo_id: int) -> Union[TODOSchema,str]:
        data = await self._repo.fetch_one_todo(todo_id=todo_id)
        return data
