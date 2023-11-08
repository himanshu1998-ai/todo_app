from typing import Union

from todo.repository.interfaces.todo_repo import ITodoREPO
from todo.schemas.schemas import TODOSchema


class UpdateTodoUsecase:
    def __init__(self, repo: ITodoREPO):
        self._repo = repo

    async def execute(self, todo: TODOSchema) -> Union[TODOSchema, str]:
        todo_data = todo.model_dump()
        title = todo_data.get('title')
        desc = todo_data.get('description')
        if title == '':
            todo_data.pop('title')
        if desc == '':
            todo_data.pop('description')
        data = await self._repo.update_todo(todo=todo_data)
        return data
