x = int(input('First Number: '))
y = int(input('Second Number: '))

def add(x, y):
    sum = x + y
    print ("Sum equals: ", sum)
    return sum
def multiply(x, y):
    product = 0
    counter = 0
    while counter < y:
        product += x
        counter += 1
    print("Product equals: ", product)
    return product

add(x, y)
multiply(x, y)