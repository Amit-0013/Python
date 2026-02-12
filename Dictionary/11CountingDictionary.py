##Write a function that takes a string and returns a dictionary with the count of each character in the string. Print the dictionary.
def count_char(s):
    count_dict = {}
    for char in s:
        count_dict[char] = count_dict.get(char , 0)+1
    return count_dict

s = "hello world"
print(count_char(s))