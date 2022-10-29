fname = '/tmp/mag.gmu.edu/git-data/dwelling/divB_simple1/GM/3d__mhd_4_e20100320-013000-000.out'
fname = '/tmp/mag.gmu.edu/git-data/swmfio/3d__var_2_e20190902-041000-000.out'

from spacepy import pybats
import numpy as np

o = pybats._probe_idlfile(fname)
print(o)

# TODO: It seems that one can just use _read_idl_bin()
# for files with only one time step.
data = pybats.IdlFile(fname, keep_case=False)

if True:
    print(data.items())
    print(data.keys())
    print(data.listunits())

if False:
    data = {}
    # the items of idlfile have type dmarray, which is a wrapped numpy array.
    # Here we remove the wrapper and place variables into a dict.
    for key, value in idlfile.items():
        data[key] = np.array(value)
