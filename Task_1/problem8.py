def palindrome(x):
    x = x.lower()
    #x == x[::-1]
    return x == ''.join(reversed(x))
        



x = input("Enter a word:")
if  palindrome(x):
    print(f"the word '{x}' is a palindrome")
else:
     print(f"the word '{x}' is not a palindrome")
