countme = 20
        
def counting(countme):
    for counter in range(countme):
        fizz = counter % 3 == 0
        buzz = counter % 5 == 0
        if fizz and buzz:
            print("fizzbuzz")
        elif fizz:
            print("fizz")
        elif buzz:
            print("buzz")
        else:
            print(counter)

counting(countme)