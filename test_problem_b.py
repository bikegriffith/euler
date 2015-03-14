# vim:filetype=python:fileencoding=utf-8

import math, operator, string
import nose.tools as NT


# Problem B
# The prime factors of 65,436 are 2, 3, 7, 19, and 41.
# What is the largest prime factor of the number 802,871,435,163?

class TestProblemB(object):

    def test_solution(self):
        NT.assert_equal(620, largest_prime_factor(802871435163))


def largest_prime_factor(n):
    # Shamelessly stolen from StackOverflow
    # http://stackoverflow.com/questions/15347174/python-finding-prime-factors
    i = 2
    while i * i < n:
        while n % i == 0:
            n = n / i
        i = i + 1
    return i
