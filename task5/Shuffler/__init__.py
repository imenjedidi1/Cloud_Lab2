import logging
from collections import defaultdict


def main(shufflerInput: list) -> dict:
    logging.info(f"Shuffling map outputs: {shufflerInput}")
    shuffled = defaultdict(list)
    for word, count in shufflerInput:
        shuffled[word].append(count)
    return dict(shuffled)
