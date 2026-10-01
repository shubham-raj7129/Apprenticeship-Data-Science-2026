import numpy as np

#Create a numpy array that is 20 columns and 20 rows
a = np.random.random((20,20))
print(a.shape)
#
# #Get the 10th row and 15th column
print(a[10,15])
#
# #Get the 3rd row
print(a[3,:])
#
# #Get the 12th column
print(a[:,12])
#
# #reverse the array
reverse_a = a[::-1]
print(reverse_a)
#
# #Print the data types in the a array
print(a.dtype)
#
# #Get the first 5 rows from the a array
c = a[:5,:]
#
# #Check is memory is share between the two arrays
print(np.may_share_memory(a,c))
#
# #Set row 2, column 1 to 0 in the c array
c[2,1] = 0
#
# #Check is a array is affected by the change
print(a[2,1])
#
# #Change to a flat list
flat_c = c.flatten()
print(flat_c.shape)
#
# #Reshape the flat list to a 3 dimensional array
new_c = flat_c.reshape(5,10,2)
print(new_c.shape)
#
# #Create a b array filled with 0s
b = np.zeros((5,5))
#
# #Check is memory is share between the two arrays
print(np.may_share_memory(a,b))
#
# #Create an array using range
d = np.array(range(8))
print(d)

# #Create an array using range
e = np.arange(8)
print(e)
#
# #Add 1 to all elements of e
print(e+1)
#
# #Square each element
print(e**2)
#
# #Double each element
e *= 2
print(e)
#
# #Get the minimum value
print(e.min())
#
# #Get the maximum value
print(e.max())
#
# #Sum the elements
print(e.sum())

