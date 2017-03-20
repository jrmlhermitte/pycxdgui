import numpy as np
from tqdm import tqdm

def runningaverage(IMGS,PF=False,rng=None):
    '''Running average using an image reader.
        Requires the current EigerImages object (with member object dims
            and lenght (len) number of frames.
        It's a more efficient way to average.
        Iavg_[n-1] = sum(Iavg,n-1)/(n-1)
        Iavg_n = ( (Iavg_[n-1])*(n-1) + I_n)/n
        Iavg_n = Iavg_[n-1] + (I_n - Iavg_[n-1])/n
        rng must be a range iterator
    '''
    if(rng is None):
        rng = range(len(IMGS))
    IAVG = np.zeros(IMGS[0].shape)
    Ivst = np.zeros(len(rng))
    print("Performing a running average")
    for i,rngno in tqdm(enumerate(rng)):
        IAVG += (IMGS[rngno] - IAVG)/float(i+1)
        Ivst[i] = np.average(IMGS[rngno])

    return IAVG,Ivst
