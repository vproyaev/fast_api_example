from pydantic import BaseModel


class MainSchema(BaseModel):
    message: str
