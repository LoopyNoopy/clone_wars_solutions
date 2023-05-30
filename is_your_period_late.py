# Kata link: https://www.codewars.com/kata/578a8a01e9fd1549e50001f1

from datetime import date

date1 = date(2016,1,1)
date2 = date(2016,1,31)
length = 30

def period_is_late(last,today,cycle_length):
    delta = today - last
    if delta.days > cycle_length:
        return True
    return False

