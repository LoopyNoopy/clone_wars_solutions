# Kata link: https://www.codewars.com/kata/559ac78160f0be07c200005a

import codewars_test as test

names = ['john McClane','Mary jeggins','tom jerry']

def name_shuffler(str_):
    split = str_.split()
    return split[1] + " " + split[0]

@test.describe("Fixed Tests")
def fixed_tests():
    @test.it('Basic Test Cases')
    def basic_test_cases():
        test.assert_equals(name_shuffler('john McClane'),'McClane john')
        test.assert_equals(name_shuffler('Mary jeggins'),'jeggins Mary')
        test.assert_equals(name_shuffler('tom jerry'),'jerry tom')