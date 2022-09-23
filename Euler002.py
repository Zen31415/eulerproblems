'''Each new term in the Fibonacci sequence is generated by adding the previous two terms. By starting with 1 and 2, the first 10 terms will be:

1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.'''

def SumFib():
    fiblist = [0, 1]
    fibsum = 0
    while fiblist[-1] <= 4000000:
        next_value = fiblist[-1] + fiblist[-2]
        fiblist.append(next_value)
        if fiblist[-1] % 2 == 0:
            fibsum += fiblist[-1]
    return(fibsum)

print(SumFib())