import numpy as np

x=[2,4,6,7,20,10,22]
y=np.array(x)

print("Mean is : ",y.mean())

print("Median is : ",np.median(y))
print("\n")
print("Mean is : ",y.mean())

print("\n")

from statistics import mode
print("Mode is:",mode([1, 1, 2, 3, 3, 3, 3, 4]))
