'''The prime factors of 13195 are 5, 7, 13 and 29.
What is the largest prime factor of the number 600851475143 ?'''

big = 600851475143

def prime_factors(big):
    # list to hold the prime factors, and a counter value
    factors = []
    x = 2
    while big > 1:
        # find numbers evenly divisible by big, count up and add them to a list
        while big % x == 0:
            factors.append(x)
            # whenever we get a hit, divide big by x
            big /= x
        x = x + 1
        # once d is as large as the square root of big, we can stop checking factors
        if x*x > big:
            if big > 1: factors.append(big)
            break
    return factors

biggestprime = max(prime_factors(big))
print(biggestprime)