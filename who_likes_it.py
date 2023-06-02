# Kata Link: https://www.codewars.com/kata/5266876b8f4bf2da9b000362

name0 = []
name1 = ["Peter"]
name2 = ["Jacob", "Alex"]
name3 = ["Max", "John", "Mark"]
name4 = ["Alex", "Jacob", "Mark", "Max"]
name5 = ["Alex", "Jacob", "Mark", "Max", "Daniel"]

name_lists = [name0, name1, name2, name3, name4, name5]


def likes(names):
    match len(names):
        case 0:
            return "no one likes this"
        case 1:
            return names[0] + " likes this"
        case 2:
            return names[0] + " and " + names[1] + " like this"
        case 3:
            return names[0] + ", " + names[1] + " and " + names[2] + " like this"
        case _:
            return names[0] + ", " + names[1] + " and " + str(len(names) - 2) + " others like this"


for name_list in name_lists:
    print(likes(name_list))

import codewars_test as test


@test.it('Basic tests')
def _():
    test.assert_equals(likes([]), 'no one likes this')
    test.assert_equals(likes(['Peter']), 'Peter likes this')
    test.assert_equals(likes(['Jacob', 'Alex']), 'Jacob and Alex like this')
    test.assert_equals(likes(['Max', 'John', 'Mark']), 'Max, John and Mark like this')
    test.assert_equals(likes(['Alex', 'Jacob', 'Mark', 'Max']), 'Alex, Jacob and 2 others like this')
