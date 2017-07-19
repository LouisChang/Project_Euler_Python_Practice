# Problem 48
def Solution(N):
    sum = 0
    for i in range(1,N+1):
        sum += i**i
        sum = int(sum % (10**10))
    return sum 

Solution(1000)
