import logging


def main(reducerInput: tuple) -> tuple:
    word, values = reducerInput
    logging.info(f"Reducing word '{word}': {values}")
    return word, sum(values)
