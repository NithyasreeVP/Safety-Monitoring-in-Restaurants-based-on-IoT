import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import style
#from scipy.stats import linregress
df1 = pd.read_csv("temp_readings3.csv", names=["Time", "Temperature"], header=None)
df1.plot(x="Time", y="Temperature")
plt.show()

df2 = pd.read_csv("hum_readings3.csv", names=["Time", "Humidity"], header=None)
df2.plot(x="Time", y="Humidity")
plt.show()

df3 = pd.read_csv("gas_readings3.csv", names=["Time", "LPG"], header=None)
df3.plot(x="Time", y="LPG")
plt.show()

df4 = pd.read_csv("co2_readings3.csv", names=["Time", "CO2"], header=None)
df4.plot(x="Time", y="CO2")
plt.show()

df5 = pd.read_csv("weight_readings3.csv", names=["Time", "Weight"], header=None)
df5.plot(x="Time", y="Weight")
plt.show()

df6 = pd.read_csv("flame_readings3.csv", names=["Time", "Flame"], header=None)
df6.plot(x="Time", y="Flame")
plt.show()
