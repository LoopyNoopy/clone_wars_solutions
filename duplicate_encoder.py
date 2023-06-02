# Kata link: https://www.codewars.com/kata/54b42f9314d9229fd6000d9c

string1 = "din"
string2 = "recede"
string3 = "Success"
string4 = "(( @"
string5 = "cTOQ(bdrW"

strings = [string1, string2, string3, string4, string5]


# My Solution
def duplicate_encode(word):
    word = word.lower()
    new_word = ""
    for letter in word:
        if word.count(letter) > 1:
            new_word = new_word + ")"
        else:
            new_word = new_word + "("
    return new_word


# Simplified
def duplicate_encode_simplified(word):
    return "".join(["(" if word.lower().count(c) == 1 else ")" for c in word.lower()])

import codewars_test as test

@test.describe("Duplicate Encoder")
def fixed_tests():
    @test.it('Basic Test Cases')
    def basic_test_cases():
        test.assert_equals(duplicate_encode("din"),"(((")
        test.assert_equals(duplicate_encode("recede"),"()()()")
        test.assert_equals(duplicate_encode("Success"),")())())","should ignore case")
        test.assert_equals(duplicate_encode("(( @"),"))((")
