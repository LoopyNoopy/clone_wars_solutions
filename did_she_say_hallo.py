# Kata link: https://www.codewars.com/kata/56a4addbfd4a55694100001f

def validate_hello(greetings):
    foreign_greeting = ['hello','ciao','hola','salut','hallo','ahoj','czesc']
    for greet in foreign_greeting:
        if greet in greetings.lower():
            return True
    else:
        return False

import codewars_test as test

@test.describe("Did She say Hallo")
def fixed_tests():
    @test.it('Basic Test Cases')
    def basic_test_cases():
        test.assert_equals(validate_hello('hello'),True)
        test.assert_equals(validate_hello('ciao bella!'),True)
        test.assert_equals(validate_hello('salut'),True)
        test.assert_equals(validate_hello('hallo, salut'),True)
        test.assert_equals(validate_hello('hombre! Hola!'),True)
        test.assert_equals(validate_hello('Hallo, wie geht\'s dir?'),True)
        test.assert_equals(validate_hello('AHOJ!'),True)
        test.assert_equals(validate_hello('czesc'),True)
        test.assert_equals(validate_hello('meh'),False)
        test.assert_equals(validate_hello('Ahoj'),True)