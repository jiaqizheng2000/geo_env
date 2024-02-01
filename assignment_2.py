# import libraries

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import pdb
import xarray as xr
import cartopy.crs as ccrs

# shared socio-economic pathways (SSPs)

# open one of the netCDF files
dset_1950_2014 = xr.open_dataset("Climate_Model_Data/tas_Amon_GFDL-ESM4_historical_r1i1p1f1_gr1_195001-201412.nc")

# python debugger
pdb.set_trace()

# explore the variables that netCDF contains
print("The variables in netCDF are:")

print(dset_1950_2014.variables.keys())

# access the temperature variables
print("the dimension of air temperature is:")
print(dset_1950_2014['tas'])
print("the type of air temperature is:")
print(dset_1950_2014['tas'].dtype)

# creation of Climate Change Maps
# mean air temperature map for 1850-1900
dset_1850_1949 = xr.open_dataset("Climate_Model_Data/tas_Amon_GFDL-ESM4_historical_r1i1p1f1_gr1_185001-194912.nc")
average_tem_1850_1900_map = np.mean(dset_1850_1949['tas'].sel(time=slice('18500101', '19001231')), axis=0)


# get approximate longitude and latitude if necessary
latitudes = dset_1850_1949.coords['lat']
longitudes = dset_1850_1949.coords['lon']

# climate scenario ssp119
# mean air temperature map for 2071-2100
# open one of the netCDF files
dset_future_ssp119 = xr.open_dataset("Climate_Model_Data/tas_Amon_GFDL-ESM4_ssp119_r1i1p1f1_gr1_201501-210012.nc")
# mean air temperature map for 2071-2100
average_tem_2071_2100_map_ssp119 = np.mean(dset_future_ssp119['tas'].sel(time=slice('20710101', '21001213')), axis=0)

# climate scenario ssp245
# mean air temperature map for 2071-2100
# open one of the netCDF files
dset_future_ssp245 = xr.open_dataset("Climate_Model_Data/tas_Amon_GFDL-ESM4_ssp245_r1i1p1f1_gr1_201501-210012.nc")
# mean air temperature map for 2071-2100
average_tem_2071_2100_map_ssp245 = np.mean(dset_future_ssp245['tas'].sel(time=slice('20710101', '21001213')), axis=0)

# climate scenario ssp585
# mean air temperature map for 2071-2100
# open one of the netCDF files
dset_future_ssp585 = xr.open_dataset("Climate_Model_Data/tas_Amon_GFDL-ESM4_ssp585_r1i1p1f1_gr1_201501-210012.nc")
# mean air temperature map for 2071-2100
average_tem_2071_2100_map_ssp585 = np.mean(dset_future_ssp585['tas'].sel(time=slice('20710101', '21001213')), axis=0)

def visualize_temperature_difference_for_scenario(average_tem_period_1,average_tem_period_2,scenario,longitudes,latitudes):
    # Create the Plot
    plt.figure(figsize=(10, 6),dpi=300)
    # Use 'imshow' to plot the 2D temperature data, assuming the data is already in a 2D array
    mappable = plt.imshow(average_tem_period_2 - average_tem_period_1, origin='lower', cmap='coolwarm',
                          interpolation='nearest')

    # Add a Colorbar
    plt.colorbar(mappable, orientation='vertical', label='Temperature (K)')

    # Label the Axes
    # Set the x and y ticks to represent the latitudes and longitudes
    plt.xticks(np.linspace(0, len(longitudes) - 1, 10),
               [f'{lon:.0f}°' for lon in np.linspace(longitudes.values.min(), longitudes.values.max(), 10)])
    plt.yticks(np.linspace(0, len(latitudes) - 1, 10),
               [f'{lat:.0f}°' for lat in np.linspace(latitudes.values.min(), latitudes.values.max(), 10)])

    # Set the labels for the x and y axes
    plt.xlabel('Longitude')
    plt.ylabel('Latitude')

    # Display the Plot
    plt.title('Average Air Temperature between 1850-1900 and 2071-2100(%s)' % scenario)
    plt.savefig("assignment_2/Average Air Temperature between 1850-1900 and 2071-2100(%s).png" % scenario)
    plt.show()


# Compute and visualize the temperature differences between 2071–2100 and 1850–1900 for ssp119.
visualize_temperature_difference_for_scenario(average_tem_1850_1900_map,average_tem_2071_2100_map_ssp119,"ssp119",longitudes,latitudes)

# Compute and visualize the temperature differences between 2071–2100 and 1850–1900 for ssp245.
visualize_temperature_difference_for_scenario(average_tem_1850_1900_map,average_tem_2071_2100_map_ssp245,"ssp245",longitudes,latitudes)

# Compute and visualize the temperature differences between 2071–2100 and 1850–1900 for ssp585.
visualize_temperature_difference_for_scenario(average_tem_1850_1900_map,average_tem_2071_2100_map_ssp585,"ssp585",longitudes,latitudes)


