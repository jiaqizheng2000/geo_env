import tools
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import pdb
import xarray as xr
from datetime import datetime, timedelta

# Load the Jeddah weather data into a Pandas dataframe
df_isd = tools.read_isd_csv("Jeddah_weather_data/41024099999.csv")

# visualize and get an overview of the ISD data for Jeddah
plot = df_isd.plot(title="ISD data for Jeddah")
plt.show()

# To convert dewpoint temperature (◦C) to relative humidity (%)
# Add a new column named ‘RH’ to the df isd dataframe
df_isd['RH'] = tools.dewpoint_to_rh(df_isd['DEW'].values,df_isd['TMP'].values)

# Calculate the HI from air temperature and relative humidity data
# Add a new column named ’HI’ as follows
df_isd['HI'] = tools.gen_heat_index(df_isd['TMP'].values, df_isd['RH'].values)

# obtain the maximum values for all columns, including the HI
print(df_isd.max())

# exact moment of the highest HI
print(df_isd.idxmax())

# transfer UTC time to local time
print(df_isd.idxmax()['HI']+timedelta(hours=3))

# get air temperature and relative humidity at the moment that has highest HI
print(df_isd.loc[["2023-08-21 10:00:00"]])

# calculate HI using daily weather data instead of hourly data
print(df_isd['TMP'].resample("1d").mean())
print(df_isd['TMP'])
df_isd['HI_daily'] = tools.gen_heat_index(df_isd['TMP'].resample("1d").mean(), df_isd['RH'].resample("1d").mean())

# Produce a figure of the HI time series for 2023
plt.figure(figsize=(10, 6),dpi=300)
plot_HI = df_isd['HI'].plot(title="HI for 2023")
plt.savefig("assignment_3/HI for 2023.png")
plt.show()

# the projected increase in air temperature from 1991–
# 2010 to 2081–2100 under the ‘middle-of-the-road’ SSP2-4.5 scenario is approximately 3°C.
# To assess the potential impact of climate change on hot spells in Jeddah, apply this projected
# warming to the air temperature data and recalculate the HI.
# Calculate the HI from air temperature and relative humidity data
# Add a new column named ’HI’ as follows
df_isd['HI_ssp245'] = tools.gen_heat_index(df_isd['TMP'].values+3, df_isd['RH'].values)

# obtain the maximum values for the HI_ssp245
print(df_isd.max())
