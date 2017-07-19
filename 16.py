# Problem 16
def Solution(N):
    number = pow(2,N)
    sum = 0
    while number > 0:
        sum += int(number % 10)
        number /= 10
    return sum

Solution(1000)
