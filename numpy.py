import numpy as np
a= [1,2,3,4,5]
b = [2, 3, 4, 5, 6]
c = [d*t for d, t in zip(a, b)]
print(sum(c))