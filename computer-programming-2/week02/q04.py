text = input("Please enter the text:")
text_list = text.split(' ')
word = ""
for i in text_list:
    if len(i) > len(word):
        word = i
print(f"The longest word: {word} ")