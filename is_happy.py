# identify if a positive interger is a happy number
# calculate the suqre of a positive interger
def square(x):
    return int(x) * int(x)

# calculate the sum of the squares of its digits in base-ten
def happy(number):
    return sum(map(square, list(str(number))))

# When the algorithm ends in a cycle of repeating numbers
# this cycle always includes the number 4
def is_happy(n):
    if n < 1 or type(n) != int:
        print('the parameter should be a positive integer')
    else:
        return (n == 1 or n > 4 and is_happy(happy(n)))
        
