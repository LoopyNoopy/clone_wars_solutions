# Kata link: https://www.codewars.com/kata/578a8a01e9fd1549e50001f1

from datetime import date

date1 = date(2016,1,1)
date2 = date(2016,1,31)
length = 30

def period_is_late(last,today,cycle_length):
    delta = today - last
    if delta.days > cycle_length:
        return True
    return False

import codewars_test as test

@test.it("Basic tests")
def basic_tests():
    test.assert_equals(period_is_late(date(2016, 6, 13), date(2016, 7, 16), 35), False)
    test.assert_equals(period_is_late(date(2016, 6, 13), date(2016, 7, 16), 28), True)
    test.assert_equals(period_is_late(date(2016, 6, 13), date(2016, 7, 16), 35), False)
    test.assert_equals(period_is_late(date(2016, 6, 13), date(2016, 6, 29), 28), False)
    test.assert_equals(period_is_late(date(2016, 7, 12), date(2016, 8, 9), 28), False)
    test.assert_equals(period_is_late(date(2016, 7, 12), date(2016, 8, 10), 28), True)
    test.assert_equals(period_is_late(date(2016, 7, 1), date(2016, 8, 1), 30), True)
    test.assert_equals(period_is_late(date(2016, 6, 1), date(2016, 6, 30), 30), False)