'''
import numpy as np 
a = np.array([[1, 2], [3, 4]], ndmin = 4) 
print (a)
print (type(a))
print (a.shape)
'''
'''
import numpy as np 
a = np.array([[1,2,3],[4,5,6]]) 
print (a.shape)
'''
'''
import numpy as np 
a = np.array([[1,2,3],[4,5,6]]) 
a.shape = (3,2) 
print(a)
'''
'''
import numpy as np 
a = np.array([[1,2,3],[4,5,6]]) 
b = a.reshape(3,2) 
print (b)
'''
'''
# an array of evenly spaced numbers 
import numpy as np 
a = np.arange(24) 
print (a)
'''
'''
# array of five zeros. Default dtype is float 
import numpy as np 
x = np.zeros(5) 
print (x)
'''
'''
import numpy as np 
x = np.zeros((5), dtype = np.int64) 
print x
'''
'''# convert list to ndarray 
import numpy as np 
x = [1,2,3] 
a = np.asarray(x) 
print(a)
'''
''' # start and stop parameters set 
import numpy as np 
x = np.arange(10,20,2) 
print x
'''
'''
import numpy as np 
a = np.arange(10) 
s = slice(2,7,2) 
print (a[s])
'''
'''
import numpy as np 
a = np.array([1,2,3,4]) 
b = np.array([10,20,30,40]) 
c = a * b 
print(c)
'''

