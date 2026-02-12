##Write a function that finds and replaces all occurrences of a given word in a file named `data.txt` with another word.

def replace(filename , old_word , new_word):
    with open(filename,'r') as file:
        text = file.read()
        new_text = text.replace(old_word , new_word)
    with open('data.txt','w') as file:
        file.write(new_text)
replace('data.txt',"female","male")