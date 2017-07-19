# Problem 6
def Solution(N):
    sum_1, sum_2 = 0,0
    for i in range(1,N+1):
        sum_1 += i*i
        sum_2 += i
    return abs(sum_1 - sum_2*sum_2)

Solution(100)
