from pydantic import BaseModel


class TODOSchema(BaseModel):
    id: int
    title: str
    description: str
