# import necessary libraries
import numpy as np
import pandas as pd
import xarray as xr
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D
import tools

# Load the dataset using the open dataset function from the xarray mo
dset = xr.open_dataset(r"/Users/zhengj/PycharmProjects/geo_env/assignment_6/ERA5_Data/download.nc")

# Convert the air temperature ("t2m") from K to ◦C and precipitation (tp) from m/h to mm/h
# for more intuitive interpretation
dset["t2m"] = dset["t2m"] - 273.15
dset["tp"] = dset["tp"] * 1000

# # location of the Wadi Murwani reservoir
# specific_latitude = 22.179916674507247
# specific_longitude = 39.572559325454
# # Define the location of the Wadi Murwani reservoir:
# selected_location = dset.sel(latitude=specific_latitude, longitude=specific_longitude, method="nearest")

# # Create the figure and axes
# fig, ax1 = plt.subplots()
#
# get all information about the data
# print(selected_location["tp"])
#
# # Plot temperature data
# temp_line = selected_location["t2m"].plot.line(x="time", label="T [°C]", ax=ax1, color='blue')
# ax1.set_ylabel('Temperature (°C)', color='blue')
#
# # Create the second y-axis for precipitation data
# ax2 = ax1.twinx()
# precip_line = selected_location["tp"].plot.line(x="time", label="P [mm]", ax=ax2, color='red')
# ax2.set_ylabel('Precipitation (mm)', color='red')
#
# # Set the legend manually with custom color labels and position it in the upper left corner
# custom_lines = [Line2D([0], [0], color='blue', lw=4),
#                 Line2D([0], [0], color='red', lw=4)]
# ax1.legend(custom_lines, ['T [°C]', 'P [mm]'], loc='upper left')
# ax2.legend(custom_lines, ['T [°C]', 'P [mm]'], loc='upper left')
#
# # Set your desired title
# ax1.set_title("Temperature and Precipitation Time Series")
#
# # Redisplay the desired title after clearing potential xarray-generated titles
# ax2.set_title("Temperature and Precipitation Time Series")
#
# # Show the plot
# plt.show()

# # Resample the precipitation data to an annual time step and calculate the mean
# annual_precip = selected_location['tp'].resample(time='A').mean()
# print("annual_precip",annual_precip)

# Calculation of Potential Evaporation
tmin = dset["t2m"].resample(time="D").min().values
tmax = dset["t2m"].resample(time="D").max().values
tmean = dset["t2m"].resample(time="D").mean().values
lat = 21.25
doy = dset["t2m"].resample(time="D").mean().time.dt.dayofyear.values

# Compute the PE
pe = tools.hargreaves_samani_1982(tmin, tmax, tmean, lat, doy)
pe_s = pe[:,0,0,0]

# Plot the PE time series
daily_time = pd.to_datetime(dset['time'].values).normalize().unique()
plt.figure(figsize=(10, 6), tight_layout=True)
plt.plot(daily_time, pe_s, label="Potential Evaporation")
plt.xlabel("Date")
plt.ylabel("PE [mm day−1]")
plt.title("Potential Evaporation Time Series")
plt.grid(True)
plt.show()

# mean annual PE
pe_series = pd.Series(pe_s, index=daily_time)
annual_mean_pe = pe_series.resample("A").mean()
mean_annual_pe = annual_mean_pe.mean()
print(mean_annual_pe)