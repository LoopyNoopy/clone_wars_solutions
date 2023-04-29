# Kata link: https://www.codewars.com/kata/525f50e3b73515a6db000b83

number = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]


def create_phone_number(n):
    n.insert(0, "(")
    n.insert(4, ") ")
    n.insert(8, "-")
    n = [str(x) for x in n]
    n = "".join(n)
    return n


# Simplified solution
def simplified_create_phone_number(n):
    return "({}{}{}) {}{}{}-{}{}{}{}".format(*n)


print(create_phone_number(number))
number = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]  # Original breaks the original list
print(simplified_create_phone_number(number))
