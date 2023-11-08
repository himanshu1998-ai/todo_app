import os
from common.config import CREATE_TODO, FETCH_ONE_TODO, FETCH_ALL_TODO, UPDATE_TODO, DELETE_TODO
import uvicorn
from fastapi import FastAPI
from todo.schemas.schemas import TODOSchema
from todo.repository.impl.todo_store import TodoStore
from todo.usecases.create.create_todo import CreateTodoUsecase
from todo.usecases.read.fetch_one import FetchOneTodoUsecase
from todo.usecases.read.fetch_all import FetchAllTodoUsecase
from todo.usecases.update.update_todo import UpdateTodoUsecase
from todo.usecases.delete.delete_todo import DeleteTodoUsecase

app = FastAPI()

repo = TodoStore(db_name=os.getenv("DB_NAME"), collection_name=os.getenv("COLLECTION_NAME"))


@app.post(CREATE_TODO)
async def create_todo(todo: TODOSchema):
    usecase = CreateTodoUsecase(repo=repo)
    response = await usecase.execute(todo=todo)
    return response


@app.get(FETCH_ONE_TODO)
async def fetch_one_todo(todo_id: int):
    usecase = FetchOneTodoUsecase(repo=repo)
    response = await usecase.execute(todo_id=todo_id)
    return response

@app.get(FETCH_ALL_TODO)
async def fetch_all_todo():
    usecase = FetchAllTodoUsecase(repo=repo)
    response = await usecase.execute()
    return response


@app.put(UPDATE_TODO)
async def update_todo(todo: TODOSchema):
    usecase = UpdateTodoUsecase(repo=repo)
    response = await usecase.execute(todo=todo)
    return response


@app.delete(DELETE_TODO)
async def delete_todo(todo_id: int):
    usecase = DeleteTodoUsecase(repo=repo)
    response = await usecase.execute(todo_id=todo_id)
    return response

if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0', port=5007)
