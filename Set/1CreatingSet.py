##Create a set with the first 10 positive integers. Print the set.
st = set()
for i in range(11):
    st.add(i)
print("Original Set: ",st)

##Add the number 11 to the set created in Assignment 1. Then remove the number 1 from the set. Print the modified set.
st.add(11)
st.remove(1)
print("Modified Set: ",st)

##Create a new set containing only the even numbers from the set created in Assignment 1 using a set comprehension. Print the new set.
new_set = {i for i in st if i%2==0}
print("Set after filtering: ",new_set)