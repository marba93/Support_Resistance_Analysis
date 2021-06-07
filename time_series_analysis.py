import pandas as pd
import numpy as np
# import matplotlib
# import matplotlib.pyplot as plt


# input data

df = pd.read_csv(r"/Users/marcosbrionesalvarez/Downloads/Price and Support-Resistance Data Sept 2018 - Dec 2020 (Version 2).csv")
print(df)
df = df[df['Type']=='Copper']
cols_to_drop = ['Type', 'country', 'form', 'perUnit', 'CNY',
       'INR', 'KRW', 'EUR', 'JPY', 'GBP', 'Support', 'Resistance']
df.drop(cols_to_drop, axis=1, inplace=True)
df = df.set_index('collectionTime')
print(df)
