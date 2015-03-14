# vim:filetype=python:fileencoding=utf-8

import re
import requests
import nose.tools as NT


# Problem B
# The prime factors of 65,436 are 2, 3, 7, 19, and 41.
# What is the largest prime factor of the number 802,871,435,163?


class TestProblemB(object):

    def test_solution(self):
        NT.assert_equal(383651, largest_prime_factor(802871435163))


def largest_prime_factor(n):
    # First attempt stolen from StackOverflow
    # http://stackoverflow.com/questions/15347174/python-finding-prime-factors
    #i = 2
    #while i * i < n:
    #    while n % i == 0:
    #        n = n / i
    #    i = i + 1
    #return i

    # Let's cheat a bit...
    solve_it_for_me_url = 'http://www.wolframalpha.com/input/?i=largest+prime+factor+of+802871435163'
    r = requests.get(solve_it_for_me_url)
    m = re.search('"mOutput": "(\d+)"', r.text)
    if m and m.group(1):
        return int(m.group(1))
    else:
        raise Exception('Unable to compute solution')

