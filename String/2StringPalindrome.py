## Write a Python program to check if a string is a palindrome.
word = input("Enter the word: ")
r_word = word[::-1]
if word == r_word:
    print("The string is palindrome.")
else:
    print("The string is not palindrome.")