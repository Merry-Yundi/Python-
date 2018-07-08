# calculate fact of a non-negative interger
def fact(n):
    if n == 1:
        return 1
    else:
       return n * fact(n-1)

# calculate the sum of factotial of each numbers equal to or below n
def sum_fact(n):
    if n < 0 or type(n) != int:
        print('the parameter should be a non-negative integer')
    else:
        sum = 0
        for i in range(1,n+1):
            sum = sum + fact(i)
        return sum 
