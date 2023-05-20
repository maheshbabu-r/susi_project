import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Path: main.py

# this is for testing purposes
df = pd.read_csv('data/2019.csv')
# df = df.dropna()
# df = df.drop(columns=['Unnamed: 0'])
# df = df.drop(columns=['Unnamed: 0.1'])
# df = df.drop(columns=['Unnamed: 0.1.1'])
# df = df.drop(columns=['Unnamed:
# df = df.drop(columns=['Unnamed:

# write pandas all important dataframe inspection code
print(df.head())
print(df.info())
print(df.describe())
print(df.columns)
print(df.shape)
print(df.isnull().sum())
print(df.dtypes)
print(df['Country or region'].unique())
print(df['Country or region'].nunique())
print(df['Country or region'].value_counts())
print(df['Country or region'].value_counts().head(10))
print(df['Country or region'].value_counts().tail(10))
print(df['Country or region'].value_counts().sort_index())
print(df['Country or region'].value_counts().sort_index(ascending=False))
print(df['Country or region'].value_counts().sort_values())
print(df['Country or region'].value_counts().sort_values(ascending=False))
