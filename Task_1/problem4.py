def reverse_words(x):
        y = x.split(" ")
        rev_words = []
        for i in y:
            rev_words.append(i[::-1])
        new_x = " ".join(rev_words)
        return new_x

x = input("Enter a sentence:")
print ("the new sentence:",reverse_words(x))

    
