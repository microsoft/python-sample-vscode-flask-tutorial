import numpy as np
from pudb import set_trace

set_trace()

a = np.arange(10)

print(a)  # silence pyflakes
print(a[8])
print(a[9])
Plataforma = 2
for i in a:
    if i == Plataforma:  # silence pyflakes
        print(i)
