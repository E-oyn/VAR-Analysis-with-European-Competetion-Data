#Step 1: Importing the Libraries
import csv
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import operator
import statsmodels.api as sm
from statsmodels.tsa.stattools import grangercausalitytests
from statsmodels.tsa.stattools import adfuller
from statsmodels.tsa.api import VAR

#Define and read the Data

df = pd.read_csv('var_data.csv')
#Defining the headers
df.head()
#df = df.copy()
#Leaving only German Data

df = df[df['country_n'] == 'Germany']
df = df[df['sec'] == 'Mc']

#Sorting the Data
df.sort_values(by=['country_n', 'sec', 'year', 'size'], ascending=False)
#df.info()

df1 = df[['year','size', 'hhi', 'markup', 'TFP', 'interest', 'sec']]
#df1 = df1.copy()
nan_value = float("NaN")
df1.replace("",nan_value, inplace=True)
df1.dropna(inplace=True)

df1 = df1[df1['size'] == 1]

plt.title("Test Plot")

print(df1)

plt.subplot(2, 2, 1)
plt.plot(df1.year, df1.interest)
plt.title("Interest")
plt.tight_layout()

plt.subplot(2, 2, 2)
plt.plot(df1.year, df1.markup)
plt.title("Markup")
plt.tight_layout()

plt.subplot(2, 2, 3)
plt.plot(df1.year, df1.hhi)
plt.title("Herfindahl-Hirschman Index")
plt.tight_layout()

plt.subplot(2, 2, 4)
plt.plot(df1.year, df1.TFP)
plt.title("Total Factor Productivity")
plt.tight_layout()

plt.show()


df1.to_csv(r'C:\Users\Ege\Dropbox\Sose 21\Python\expo1.csv')