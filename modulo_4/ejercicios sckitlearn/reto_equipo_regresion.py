import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, median_absolute_error, r2_score

df = pd.read_csv('../data/science_data.csv')
print("Primeras filas dataset")
print(df.head(5))

print(df.describe())

#corr_per = df[['temperatura','edad']].corr(method="pearson")

#print(corr_per)
