# Kata link: https://www.codewars.com/kata/5656b6906de340bd1b0000ac

a = "xyaabbbccccdefww"
b = "xxxxyyyyabklmopq"
c = "abcdefghijklmnopqrstuvwxyz"

def longest(a1, a2):
    return "".join(sorted(set(a1+a2)))

print(longest(a,b))
print(longest(c,c))

import codewars_test as test


@test.describe("longest")
def fixed_tests():
    @test.it("basic tests")
    def basics():
        test.assert_equals(longest("aretheyhere", "yestheyarehere"), "aehrsty")
        test.assert_equals(longest("loopingisfunbutdangerous", "lessdangerousthancoding"), "abcdefghilnoprstu")
        test.assert_equals(longest("inmanylanguages", "theresapairoffunctions"), "acefghilmnoprstuy")