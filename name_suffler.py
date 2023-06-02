# Kata link: https://www.codewars.com/kata/559ac78160f0be07c200005a

names = ['john McClane','Mary jeggins','tom jerry']

def name_shuffler(str_):
    split = str_.split()
    return split[1] + " " + split[0]

for name in names:
    print(name_shuffler(name))