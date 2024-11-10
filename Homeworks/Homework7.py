#Load the Data
import pandas as pd
import numpy
import matplotlib.pyplot as plt
data1 = pd.read_csv("global_air_quality.csv")
data1

#Make a New Column
data1["PM25_Value"] = data1["FactValueNumeric"]
print(data1[["FactValueNumeric", "PM25_Value"]])

#Calculate Average PM2.5 Concentration
averagepm25 = data1.groupby("ParentLocation")["PM25_Value"].mean().reset_index()
averagepm25.rename(columns={"PM25_Value": "Average_PM25"}, inplace = True)
data1 = data1.merge(averagepm25, on="ParentLocation", how="left")
print(data1[["Location", "ParentLocation", "PM25_Value", "Average_PM25"]])

#Analyze Data
#The Eastern Mediterranean areas have the most air pollution and this surprises me cause I thought that it had good air quality!!

#Save the Processed Data: I didn't know how to submit a Jupyter Notebooks through gradescope because it kept saving weirdly. That's why I am submitting my code through Gradescope.

#Create a Scatter Plot
import seaborn as sns
import matplotlib.pyplot as plt
df = sns.load_dataset("planets")
plt.figure(figsize=(12,4))
sns.scatterplot(data=df, x='orbital_period', y='mass', hue='method', palette='viridis')
plt.xscale("log")
plt.yscale("log")
plt.title("Relationship Between Orbital Period and Mass of Explanets")
plt.xlabel("Orbital Period")
plt.ylabel("Mass")
plt.legend(title="Discovery Method", loc="upper left", bbox_to_anchor=(1,1))
plt.tight_layout()
plt.show()

#Create a Bar Chart
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
df = sns.load_dataset("planets")
df_clean = df.dropna(subset=['year', 'method'])
count_df = df_clean.groupby(['year', 'method']).size().reset_index(name='count')
plt.figure(figsize=(12, 4))
sns.barplot(data=count_df, x='year', y='count', hue='method', palette='Set2')
plt.title("The Number of Exoplanets Discovered Each Year")
plt.xlabel('Year')
plt.ylabel('Number of Exoplanets Discovered')
plt.legend(title="Discovery Method", loc="upper left", bbox_to_anchor=(1,1))
plt.show()