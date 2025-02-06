def perfectNum(x):
    divSum =0
    for i in range(1,x):
        if x % i == 0:
            divSum +=i
    return divSum == x        


x = int(input("Enter positive integer:"))
if perfectNum(x):
    print(f"{x} is a perfect number")
else:
     print(f"{x} is not a perfect number")