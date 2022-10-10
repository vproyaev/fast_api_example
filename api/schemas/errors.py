from pydantic import BaseModel


class PhraseExpressionError(BaseModel):
    error: str | None
    detail: str | None
