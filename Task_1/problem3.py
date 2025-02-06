def sumOfDigits(x):
    sum = 0
    while x>0:
        digit =  x % 10
        sum +=digit
        x = x//10
    return sum

x = int(input("Enter positive integer:"))
if x < 0 :
    print("Enter a positive integer!")
else:
    sum = sumOfDigits(x)
    print("total sum of digits:", sum)

