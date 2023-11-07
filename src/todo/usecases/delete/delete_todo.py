from typing import Union
from todo.repository.interfaces.todo_repo import ITodoREPO


class DeleteTodoUsecase:
    def __init__(self, repo: ITodoREPO):
        self._repo = repo

    async def execute(self, todo_id: int) -> Union[int, str]:
        data = await self._repo.delete_todo(todo_id=todo_id)
        return data
