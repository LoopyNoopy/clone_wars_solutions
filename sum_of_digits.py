# Kata link: https://www.codewars.com/kata/541c8630095125aba6000c00

numbers = [16, 942, 132189, 493193]


def digital_root(n):
    iterate = 0
    final = 0
    final = n
    while len(str(final))>1:
        for digit in str(final):
            iterate += int(digit)
            final = iterate
    return iterate

import codewars_test as test

@test.describe("Sum of Digits / Digital Root")
def fixed_tests():
    @test.it('Basic Test Cases')
    def basic_test_cases():
        test.assert_equals(digital_root(16), 7)
        test.assert_equals(digital_root(942), 6)
        test.assert_equals(digital_root(132189), 6)
        test.assert_equals(digital_root(493193), 2)