def count(text):
    with open (text, "r", encoding="utf-8") as file:
        words = file.read().split().lower()
    
    count_word ={}
    for i in words:
        count_word[i]= count_word.get(i, 0)+1

    return count_word

text = input("enter the name of the text_file: ")
for i, j in count(text).items():
    print(f"{i}: {j}")