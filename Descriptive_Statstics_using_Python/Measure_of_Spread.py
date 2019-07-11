#Range
import numpy as np
A=np.array([[10,14,11,7,9.5,15,19],[8,9,17,14.5,12,18,15.5], [15,7.5,11.5,10,10.5,7,11],[11.5,11,9,12,14,12,7.5]])
A

B=A.T
B

a=np.ptp(B, axis=0)
b=np.ptp(B,axis=1)

print(a)
print(b)


#Quartile
A=np.array([[10,14,11,7,9.5,15,19],[8,9,17,14.5,12,18,15.5], [15,7.5,11.5,10,10.5,7,11],[11.5,11,9,12,14,12,7.5]])

B=A.T

a=np.percentile(B,27,axis=0, interpolation='lower')
b=np.percentile(B,25,axis=1, interpolation='lower')
c=np.percentile(B,75,axis=0, interpolation='lower')
d=np.percentile(B,50,axis=0, interpolation='lower')

print(a)

print(b)

print(c)

print(d)



#inter-qurtile range
import numpy as np
from scipy.stats import iqr
A=np.array([[10,14,11,7,9.5,15,19],[8,9,17,14.5,12,18,15.5] [15,7.5,11.5,10,10.5,7,11],[11.5,11,9,12,14,12,7.5]])

B=A.T

a=iqr(B, axis=0 , rng=(25, 75), interpolation='lower')
b=iqr(B, axis=1 , rng=(25, 75), interpolation='lower')

print(a,b)


#Variance

import numpy as np
A=np.array([[10,14,11,7,9.5,15,19],[8,9,17,14.5,12,18,15.5],
  [15,7.5,11.5,10,10.5,7,11],[11.5,11,9,12,14,12,7.5]])

B=A.T

a = np.var(B,axis=0)
b = np.var(B,axis=1)

print(a)

print(b)


#Standard deviation
import numpy as np
A=np.array([[10,14,11,7,9.5,15,19],[8,9,17,14.5,12,18,15.5],
  [15,7.5,11.5,10,10.5,7,11],[11.5,11,9,12,14,12,7.5]])
B=A.T
a = np.std(B,axis=0)
b = np.std(B,axis=1)
print(a)

print(b)
