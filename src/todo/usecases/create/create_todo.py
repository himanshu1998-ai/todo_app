from todo.repository.interfaces.todo_repo import ITodoREPO
from todo.schemas.schemas import TODOSchema


class CreateTodoUsecase:
    def __init__(self, repo: ITodoREPO):
        self._repo = repo

    async def execute(self, todo_id: int, todo: TODOSchema) -> str:
        data = await self._repo.create_todo(todo_id, todo)
        return data
