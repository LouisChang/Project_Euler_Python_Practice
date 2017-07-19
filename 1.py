# Problem 1
def Solution(N):
    sum = 0
    for i in range(N-1):
        if (i+1) % 3 == 0 or (i+1) % 5 == 0:
            sum += i+1
            
    return sum

Solution(1000)
