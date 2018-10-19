from context import src
from src.halos import Halos
from src import plot
from src.move import centering_com
from src.utilities import intersect

import matplotlib
import matplotlib.pyplot as plt

import pynbody as pn
import pynbody.plot.sph as sph
import pynbody.units as u

import os
import numpy as np
from scipy.optimize import curve_fit

HALO_NUMBER = 497 #after this the main halo has no subhalos
BIN_NUMBER = 100

DataFolder = "/fred/oz071/balves/"
SubhalosFolder = "Test_NOSN_NOZCOOL_L010N0128/data/subhalos_103/subhalo_103"
SnapshotFolder = "Test_NOSN_NOZCOOL_L010N0128/data/snapshot_103/snap_103.hdf5"

h = Halos(os.path.join(DataFolder,SubhalosFolder), 
          os.path.join(DataFolder,SubhalosFolder), HALO_NUMBER)
halos = h.get_halos()

print(halos[0])

c, M200, res, rel = ([] for i in range(4))
exceptions = [1,11,15,16,18,19,20,22,24]
iterable = iter([item for item in range(1,25) if item not in exceptions])
for i in iterable:
    M200.append(halos[i].properties['Halo_M_Crit200'].in_units('Msol'))
    c.append(h.concentration_200(idx=i, sub_idx=0))
    res.append(h.is_resolved(i))
    rel.append(h.is_relaxed(i))                                                                      

c_obj = plot.Concentration([c, c], extra_var=M200, name='figs/Concentration.png')
c_obj.set_all_properties(model='concentration_mass')
c_obj.scatter_plot(0, (0,0), resolved_bools=res, relaxed_bools=rel)
c_obj.scatter_plot(1, (1,0)) 
c_obj.savefig()

if __name__ == 'main':
    unittest.main()
