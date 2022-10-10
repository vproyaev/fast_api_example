from api.schemas.phrase_expression import PhraseExpression


def get_error_str_by_traceback(
    traceback_error_str: str,
    phrase: PhraseExpression
) -> str:
    error = traceback_error_str.split('\n')

    phrase_error = list(map(str.strip, error))
    phrase_index = phrase_error.index(phrase.phrase)

    error_symbol_index = len(error[phrase_index + 1])
    error_symbol = error[phrase_index][error_symbol_index - 1]

    return (
        f'{phrase_error[-2]} - '
        f'{error[phrase_index].strip()} - '
        f'Error Symbol {error_symbol}'
    )
