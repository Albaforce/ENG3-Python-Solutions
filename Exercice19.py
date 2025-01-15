unique_words = set()
i = 0 
while True:
    word = input("Enter a word: ")
    if word == "":
        break
    i += 1
    unique_words.add(word.lower())

print(f"You typed {i} words and {len(unique_words)} unique words {unique_words}.")

choice = input("wanna see the list of unique words? (y/n)")
if choice == 'y':
    with open("unique_list.txt",'w') as file :
        file.write(str(unique_words))