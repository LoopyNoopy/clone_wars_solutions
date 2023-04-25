# Complete the solution so that it returns true if the first argument(string) passed in ends with the 2nd argument (
# also a string).

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
