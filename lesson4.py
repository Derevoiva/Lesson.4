"""Lesson 4: functional programming exercises."""
from collections import Counter
from functools import reduce
from itertools import count, cycle, islice
from operator import mul

def salary(hours: float, hourly_rate: float, bonus: float) -> float:
    if hours < 0 or hourly_rate < 0: raise ValueError("Negative hours or rate")
    return hours * hourly_rate + bonus

def greater_than_previous(numbers):
    return [b for a,b in zip(numbers, numbers[1:]) if b > a]

def divisible_by_20_or_21():
    return [n for n in range(20,241) if n % 20 == 0 or n % 21 == 0]

def unique_numbers(numbers):
    frequencies = Counter(numbers)
    return [number for number in numbers if frequencies[number] == 1]

def even_number_product():
    return reduce(mul, range(100,1001,2), 1)

def consecutive_numbers(start: int, stop: int):
    return list(islice(count(start), max(stop-start+1,0)))

def repeat_items(items, limit: int):
    if limit < 0: raise ValueError("limit must be non-negative")
    return list(islice(cycle(items), limit))

def factorials(n: int):
    if n < 0: raise ValueError("n must not be negative")
    result = 1
    for i in range(1,n+1):
        result *= i
        yield result
