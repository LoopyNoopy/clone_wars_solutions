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
            print(str(final))
    return iterate


for number in numbers:
    print(digital_root(number))
