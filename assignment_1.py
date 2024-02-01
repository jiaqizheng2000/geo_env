# import libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import pdb
import xarray as xr

# Add netCDF file location
dset = xr.open_dataset("SRTMGL1_NC.003_-Data/N21E039.SRTMGL1_NC.nc")

# allow examination of variables and objects in the memory
# pdb.set_trace()

# use dest and dset.variables to explore the variables in the file
DEM = np.array(dset.variables['SRTMGL1_DEM'])

pdb.set_trace()

# close the netCDF dile
dset.close()

# visualize the data
plt.imshow(DEM,origin='lower')
cbar = plt.colorbar()
cbar.set_label("Elevation (m asl)")
# save image into png
plt.savefig("assignment_1/assignment_1.png",dpi=300)
plt.show()