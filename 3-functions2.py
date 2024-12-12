import numpy as np

#np.arange  #arr.reshape  #arr.flatten  #np.ravel


# np.arange(start,end,step)   
#step is default by one
a = np.arange(2,20,2)
print(a)


#arr.reshape((rows,cols)) 2x2 3x3 4x4
a = a.reshape((3,3))
print(a)



#arr.flatten() covert back to 1d array
a = a.flatten()
print(a)



##arr.ravel does the same thing
a = a.ravel()
print(a)


#diffrence between flatten and ravel 

#ravel is faster as it not occupy any memory (modify the original array)

#flatten is slower as it occupies memory (return a copy of the original array)