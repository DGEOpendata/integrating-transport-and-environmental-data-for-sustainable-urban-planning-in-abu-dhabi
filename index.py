python
import pandas as pd
import matplotlib.pyplot as plt

# Load datasets
transport_data = pd.read_csv('Public_Transport_Usage_2023.csv')
air_quality_data = pd.read_json('Air_Quality_Data_2023.json')

# Example analysis: Correlating transport usage with air quality
# Convert timestamp to datetime
air_quality_data['timestamp'] = pd.to_datetime(air_quality_data['timestamp'])

# Resample air quality data to daily mean
daily_air_quality = air_quality_data.resample('D', on='timestamp').mean()

# Group transport data by day
transport_data['date'] = pd.to_datetime(transport_data['date'])
daily_transport_usage = transport_data.groupby('date').sum()

# Merge datasets on date
merged_data = pd.merge(daily_transport_usage, daily_air_quality, left_on='date', right_on='timestamp')

# Plotting
plt.figure(figsize=(12, 6))
plt.plot(merged_data['date'], merged_data['no2'], label='NO2 Levels')
plt.plot(merged_data['date'], merged_data['passengers'], label='Transport Usage')
plt.xlabel('Date')
plt.ylabel('Values')
plt.title('Correlation between Transport Usage and NO2 Levels')
plt.legend()
plt.show()
