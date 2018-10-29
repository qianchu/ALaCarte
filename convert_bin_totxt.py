import numpy as np
from sys import argv
import math

if __name__=='__main__':
    filepath=argv[1]
    M = np.fromfile(filepath, dtype=np.float32)
    d=int(math.sqrt(M.shape[0]))
    M=M.reshape(d,d)
    np.savetxt(filepath+'.txt',M)


