##Create a set and remove elements from it until it is empty. Print the set after each removal.
st = set()
for i in range(15):
    st.add(i)
while st:
    st.pop()
    print(st)