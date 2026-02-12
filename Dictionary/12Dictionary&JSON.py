##Create a dictionary representing a book with keys 'title', 'author', 'year', and 'genre'. 
# Convert the dictionary to a JSON string and print it.
import json
dict = {"Title":"Head first Python","Author":"Oriele","Year":1995,"Genre":"education"}
json_book = json.dumps(dict)
print(json_book)