# Problem 2
def Solution(max):
    curr = 1
    next = 2
    sum = 2
    while next < max:
        curr, next = next, curr + next
        if next % 2 == 0:
            sum += next
    return sum

Solution(4000000)
