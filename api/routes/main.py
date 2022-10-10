import traceback

from fastapi import APIRouter, Query
from starlette.responses import RedirectResponse

from api.schemas.errors import PhraseExpressionError
from api.schemas.main import MainSchema
from api.schemas.phrase_expression import PhraseExpression, PhraseExpressionAnswer, PhraseExpressionAnswerSTR
from api.support_functions.get_error_str import get_error_str_by_traceback

main_router = APIRouter()


@main_router.get(
    path='/',
    responses={
        200: {'schema': MainSchema}
    },
    tags=['hello_world'],
    description='Return phrase "Hello World".'
)
async def index() -> MainSchema:
    return MainSchema(message='Hello World')


@main_router.get(
    path='/index',
    status_code=200,
    tags=['redirect_to_main'],
    description='Redirect to main endpoint',
    response_class=RedirectResponse
)
async def redirect_to_main() -> RedirectResponse:
    response = RedirectResponse(url='/')
    return response


@main_router.get(
    path='/eval',
    responses={
        200: {'schema': PhraseExpression},
        400: {'schema': PhraseExpressionError}
    },
    tags=['eval_get'],
    description=(
        'Executes the passed "phrase" expression with the '
        '"eval" method.'
    )
)
async def eval_get(
    phrase: str = Query(None, alias='phrase')
) -> PhraseExpressionAnswerSTR | PhraseExpressionError:
    try:
        return PhraseExpressionAnswerSTR(answer=f'{phrase}={int(eval(phrase))}')
    except Exception:
        return PhraseExpressionError(
            detail='The expression was passed in error, try again.'
        )


@main_router.post(
    path='/eval',
    status_code=201,
    responses={
        201: {'schema': PhraseExpression},
        400: {'schema': PhraseExpressionError}
    },
    tags=['eval_post'],
    description=(
        'Executes the passed "phrase" expression with the '
        '"eval" method and return it in json.'
    )
)
async def eval_post(
    phrase: PhraseExpression
) -> PhraseExpressionAnswer | PhraseExpressionError:
    try:
        return PhraseExpressionAnswer(answer=eval(phrase.phrase))
    except Exception:
        error = get_error_str_by_traceback(
            traceback.format_exc(), phrase
        )
        return PhraseExpressionError(error=error)
