class TODO:
    def __init__(self, todo_id: int, title: str, description: str,):
        self.todo_id = todo_id
        self.title = title
        self.description = description

    @classmethod
    def from_json(cls, json):
        return cls(**json)

    def to_json(self):
        return self.__dict__.copy()

