from typing import Union, List

from todo.repository.interfaces.todo_repo import ITodoREPO
from todo.schemas.schemas import TODOSchema


class FetchAllTodoUsecase:
    def __init__(self, repo: ITodoREPO):
        self._repo = repo

    async def execute(self) -> Union[List[TODOSchema], str]:
        data = await self._repo.fetch_all_todo()
        return data
