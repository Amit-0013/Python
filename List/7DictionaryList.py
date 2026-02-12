##Create a list of dictionaries where each dictionary represents a student with keys 'name' and 'score'. Sort the list of dictionaries by the 'score' in descending order and print the sorted list.
lst = [ {"Name":"Amit", "Score":32},
         {"Name":"Harsh","Score":33},
         {"Name":"Rishi","Score":31}
        ]
sorted_list = sorted(lst , key = lambda x: x['Score'],reverse=True)
print("The sorted list is: ")
for studs in sorted_list:
    print(studs)