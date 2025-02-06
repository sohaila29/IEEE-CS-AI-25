def odd_nums (x):
    for i in range (1, x):
        if(i%2 == 1):
            print(i )

x = int(input("Enter positive integer:"))
if x <=0:
    print ("Enter positive integer!")
else:
    print(odd_nums(x))