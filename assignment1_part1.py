#!/usr/bin/env/python
# -*- coding: utf-8 -*-
"""Assignment 1"""


def listDivide(numbers, divide=2):
    """A function that returns the number of elements in the numbers
    list that are divisible by divide.

    Args:
        numbers (list): A list of integers.
        divide (int):  Default value of 2.

    Returns:
        len(num)(int): Length of the list of numbers divisible by divide.

    Examples:
        >>>listDivide([1, 2, 3, 4, 5])
        2

        >>>listDivide([2, 4, 6, 8, 10])
        5
    """

    num = []
    for x in numbers:
        if x % divide == 0:
            num.append(numbers)
    return len(num)


class ListDivideException(Exception):
    """Exception class"""
    pass


def testListDivide():
    """Performs tests on the function listDivide."""

    result = listDivide([1, 2, 3, 4, 5])
    if result != 2:
        raise ListDivideException('Fail!')
    result = listDivide([2, 4, 6, 8, 10])
    if result != 5:
        raise ListDivideException('Fail!')
    result = listDivide([30, 54, 63, 98, 100], divide=10)
    if result != 2:
        raise ListDivideException('Fail!')
    result = listDivide([])
    if result != 0:
        raise ListDivideException('Fail!')
    result = listDivide([1, 2, 3, 4, 5], 1)
    if result != 5:
        raise ListDivideException('Fail!')


testListDivide()