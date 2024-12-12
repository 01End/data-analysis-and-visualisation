.import numpy as np

#print('1d array')
a = np.array([1,2,3,4,5])

#print('2d array')
b = np.array([[1,2,3,4,5],[6,7,8,9,10]])

#print('3d array')
c = np.array([[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15]])
print('2d array')
print(b)
print('1d array size')
print(a.size)
print('2d array size')
print(b.size)
print('3d array size')
print(c.size)

#shape=(rows,cols)
print('shape of arrays')
print(a.shape)
print(b.shape)
print(c.shape)


#transpose = cols to rows | rows to cols
#c = np.array([[1,2,3,4,5],
#              [6,7,8,9,10],
#              [11,12,13,14,15]])
print(c.transpose())



