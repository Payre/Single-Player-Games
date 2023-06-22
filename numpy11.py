import numpy

'''a = np.ones((5,5), dtype='int32')
a[2,2] = 9
a[1,1:4] = 0
a[1:4,1] = 0
a[1:4,3] = 0
a[3,1:4] = 0
print(a)'''


#this is a better different.
a=np.ones((5,5), dtype='int32')
z = np.zeros((3,3), dtype='int32')
z[1,1] = 9
a[1:4,1:4]=z
print(a)



n, m = map(int, input().split()) # taking number of rows and column
array = numpy.array([input().strip().split() for _ in range(n)], int)

