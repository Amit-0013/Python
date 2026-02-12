##Create a new list containing the squares of the first 10 positive integers using a list comprehension. Print the new list.
nums =[num ** 2 for num in range(1,11)]
print(nums)
##Create a new list containing only the even numbers from the list created in Assignment 1 using a list comprehension. Print the new list.
new_num =[n**2 for n in range(1,11) if n%2==0]
print(new_num)