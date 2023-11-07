from pydantic import BaseModel


class TODOSchema(BaseModel):
    title: str
    description: str
