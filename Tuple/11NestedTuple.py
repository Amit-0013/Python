##Create a nested tuple and iterate over the elements, printing each element.
nested_tuple = ((1,2,3),
                ('a','b','c'),
                ("Hello","HI","Bye")
                )
for sub_tuple in nested_tuple:
    for item in sub_tuple:
        print(item)