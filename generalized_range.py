# coding=utf-8
# Copyright (c) 2025 Jifeng Wu
# Licensed under the MIT License. See LICENSE file in the project root for full license information.
from typing import Callable, Iterator, TypeVar


T = TypeVar('T')

def generalized_range(start, stop, step, comparator, successor):
    # type: (T, T, int, Callable[[T, T], bool], Callable[[T], T]) -> Iterator[T]
    """
    A generalized range generator that yields a sequence of values, starting at `start`, and ending before `stop`.
    Comparison and increment logic are customizable via comparator and successor functions.

    Args:
        start (T): First element to yield.
        stop (T): Iteration stops just before reaching this element, as determined by comparator.
        step (int): Number of successor function applications per iteration (must be positive).
        comparator (Callable[[T, T], bool]): Returns True if current element is within range.
        successor (Callable[[T], T]): Function to give the next element in the sequence.

    Yields:
        T: Next value in the sequence.

    Raises:
        ValueError: If step is not a positive integer.
    """
    if step <= 0:
        raise ValueError('step must be a positive integer')

    current = start
    while comparator(current, stop):
        yield current
        for _ in range(step):
            current = successor(current)