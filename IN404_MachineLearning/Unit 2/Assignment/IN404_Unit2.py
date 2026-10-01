import numpy as np

sep = "=" * 50

#Create a numpy array that is 20 columns and 20 rows
a = np.random.random((20,20))
print("1. Shape of array a (20x20):")
print(a.shape)
print("\n" + sep)
#
# #Get the 10th row and 15th column
print("2. Value at row 10, column 15:")
print(a[10,15])
print("\n" + sep)
#
# #Get the 3rd row
print("3. The 3rd row:")
print(a[3,:])
print("\n" + sep)
#
# #Get the 12th column
print("4. The 12th column:")
print(a[:,12])
print("\n" + sep)
#
# #reverse the array
reverse_a = a[::-1]
print("5. Reversed array:")
print(reverse_a)
print("\n" + sep)
#
# #Print the data types in the a array
print("6. Data type of array a:")
print(a.dtype)
print("\n" + sep)
#
# #Get the first 5 rows from the a array
c = a[:5,:]
#
# #Check is memory is share between the two arrays
print("7. Do arrays a and c share memory?")
print(np.may_share_memory(a,c))
print("\n" + sep)
#
# #Set row 2, column 1 to 0 in the c array
c[2,1] = 0
#
# #Check is a array is affected by the change
print("8. Value of a[2,1] after setting c[2,1] = 0:")
print(a[2,1])
print("\n" + sep)
#
# #Change to a flat list
flat_c = c.flatten()
print("9. Shape of flattened c:")
print(flat_c.shape)
print("\n" + sep)
#
# #Reshape the flat list to a 3 dimensional array
new_c = flat_c.reshape(5,10,2)
print("10. Shape after reshaping to 3D:")
print(new_c.shape)
print("\n" + sep)
#
# #Create a b array filled with 0s
b = np.zeros((5,5))
#
# #Check is memory is share between the two arrays
print("11. Do arrays a and b share memory?")
print(np.may_share_memory(a,b))
print("\n" + sep)
#
# #Create an array using range
d = np.array(range(8))
print("12. Array created using range(8):")
print(d)
print("\n" + sep)

# #Create an array using range
e = np.arange(8)
print("13. Array created using arange(8):")
print(e)
print("\n" + sep)
#
# #Add 1 to all elements of e
print("14. Add 1 to all elements of e:")
print(e+1)
print("\n" + sep)
#
# #Square each element
print("15. Square each element of e:")
print(e**2)
print("\n" + sep)
#
# #Double each element
e *= 2
print("16. Double each element of e:")
print(e)
print("\n" + sep)
#
# #Get the minimum value
print("17. Minimum value of e:")
print(e.min())
print("\n" + sep)
#
# #Get the maximum value
print("18. Maximum value of e:")
print(e.max())
print("\n" + sep)
#
# #Sum the elements
print("19. Sum of all elements of e:")
print(e.sum())
