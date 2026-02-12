##Create a nested list representing a 3x3 matrix and print the matrix. Access and print the element at the second row and third column.
matrix =[
         [1,2,3],
         [4,5,6],
         [7,8,9]]
print("Matrix: ")
for row in matrix:
    print(row)
print("Element at second row and third column: ",matrix[1][2])