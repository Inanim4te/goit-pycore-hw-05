import re
from typing import Callable

def generator_numbers(text: str):
    regex = r'(?<=\s)\d+\.\d+(?=\s)'
    matches = re.findall(regex, text)
    for match in matches:
        yield float(match)

def sum_profit(text: str, func: Callable):
    return sum(func(text))
