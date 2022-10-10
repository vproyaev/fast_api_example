from pydantic import BaseModel


class PhraseExpression(BaseModel):
    phrase: str


class PhraseExpressionAnswer(BaseModel):
    answer: float


class PhraseExpressionAnswerSTR(BaseModel):
    answer: str
