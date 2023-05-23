# Kata link: https://www.codewars.com/kata/56a4addbfd4a55694100001f

def validate_hello(greetings):
    foreign_greeting = ['hello','ciao','hola','salut','hallo','ahoj','czesc']
    for greet in foreign_greeting:
        if greet in greetings.lower():
            return True
    else:
        return False