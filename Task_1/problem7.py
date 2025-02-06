def prime_factor(x):
    fac = []
    i = 2
    while i*i <= x: 
        if x % i == 0: 
            fac.append(i)
            while x %i ==0:
                x = x // i 
        i += 1

    if x > 1:
        fac.append(x)
    return fac



x = int(input("Enter positive integer: "))
if x <= 0:
    print("Enter a positive integer!")
else:
    print("Prime factors:", ", ".join(str(i) for i in prime_factor(x)))