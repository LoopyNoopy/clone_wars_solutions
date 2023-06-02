# Kata Link: https://www.codewars.com/kata/51f2d1cafc9c0f745c00037d

# Original Solution
def solution(text, ending):
    if text.endswith(ending):
        return True
    else:
        return False


# Better Solution
def revised_solution(text, ending):
    return text.endswith(ending)


print(solution('abc', 'bc'))  # returns true
print(solution('abc', 'd'))  # returns false

print(revised_solution('abc', 'bc'))  # returns true
print(revised_solution('abc', 'd'))  # returns false

import codewars_test as test
from random import randint

fixed_tests_True = (
    ( "samurai", "ai"    ),
    ( "ninja",   "ja"    ),
    ( "sensei",  "i"     ),
    ( "abc",     "abc"   ),
    ( "abcabc",  "bc"    ),
    ( "fails",   "ails"  ),
)

fixed_tests_False = (
    ( "sumo",    "omo"   ),
    ( "samurai", "ra"    ),
    ( "abc",     "abcd"  ),
    ( "ails",    "fails" ),
    ( "this",    "fails" ),
    ( "spam",    "eggs"  )
)

@test.describe("Fixed Tests")
def fixed_tests():
    @test.it("True Cases")
    def test_case():
        for text, ending in fixed_tests_True:
            test.assert_equals(solution(text, ending), True)
    @test.it("False Cases")
    def test_case():
        for text, ending in fixed_tests_False:
            test.assert_equals(solution(text, ending), False)
