'''If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.'''
countme = 1000

def counting(countme):
    euler1 = 0
    for counter in range(countme):
        threes = counter % 3 == 0
        fives = counter % 5 == 0
        if threes or fives:
            euler1 = euler1 + counter
    print(euler1)

counting(countme)