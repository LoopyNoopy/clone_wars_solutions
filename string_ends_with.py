# Kata Link: https://www.codewars.com/kata/51f2d1cafc9c0f745c00037d

# Original Solution
def solution(text, ending):
    if text.endswith(ending):
        return True
    else:
        return False


# Better Solution
def revised_solution(text, ending):
    return text.endswith(ending)


print(solution('abc', 'bc'))  # returns true
print(solution('abc', 'd'))  # returns false

print(revised_solution('abc', 'bc'))  # returns true
print(revised_solution('abc', 'd'))  # returns false
