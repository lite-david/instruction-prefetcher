import sys
import numpy as np

def geo_mean(iterable):
    a = np.array(iterable)
    return a.prod()**(1.0/len(a))

fname = sys.argv[1]
f = open(fname,'r')
flines = f.readlines()
f.close()
vals = []
for l in flines:
    sl = l.split(',')
    vals.append(float(sl[-1].strip()))
print(vals)
print(geo_mean(vals))
