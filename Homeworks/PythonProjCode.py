import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import scipy.optimize as fit

df = pd.read_csv('3856678.csv') # Initially I had an .nc data file and I had a hard time actually figuring out how to open it because it required me to import two new things I didn't know how to use, but I eventually found this
print(df)
df_filtered = df[['LATITUDE', 'HPCP']]
print(df_filtered) #Filtering so that I get yearly precipitation at all Longitudes of Colorado
plt.figure()
plt.scatter(df_filtered['LATITUDE'], df_filtered['HPCP'], label='Average Precipitation')
plt.title('Average Precipitation From 2013-2014 Recorded for Latitude in Colorado')
plt.yscale('log') #Because there are so many random anomalies in this dataset and I thought it would be best to represent it on a log scale when without the log scale, it looked like a bunch of 0 values and a few 1000 mm values.
plt.xscale('log')
plt.xlabel('Latitude')
plt.ylabel('Average Precipitation')
plt.legend()
plt.show()

#Super random model with a lot of noise so I will try to see if I can use a linear function to curve fit it, because nothing else will even work.
def f(x, m, b):
    return m * x + b
p0 = [1, 0.1]

#Actually fitting the curve
parameters, covariance = fit.curve_fit(f, df_filtered['LATITUDE'], df_filtered['HPCP'], p0)
print(parameters)
print(covariance)


print(f"Optimized parameters: m = {parameters[0]}, b = {parameters[1]}")
x_fit = np.linspace(min(df_filtered['LATITUDE']), max(df_filtered['LATITUDE']), 100)
y_fit = f(x_fit, *parameters)
plt.scatter(df_filtered['LATITUDE'], df_filtered['HPCP'], label='Average Precipitation')
plt.plot(x_fit, y_fit, color='red', label='Fitted Line')
plt.title('Fitted Line for Precipitation vs Latitude')
plt.yscale('log')
plt.xscale('log')
plt.xlabel('Latitude')
plt.ylabel('Average Precipitation')
plt.legend()
plt.show()

#Error Analysis
y_observed = df_filtered['HPCP']
y_model = f(df_filtered['LATITUDE'], *parameters)
residuals = y_observed - y_model
#I don't know how to find the sigma value given this dataset, but if I was able to find it it would be
#chi_squared = np.sum((residuals**2) / sigma**2)
degrees_of_freedom = len(df_filtered) - len(parameters)
#print(f"Chi-squared: {chi_squared}")
print(f"Degrees of freedom: {degrees_of_freedom}")

