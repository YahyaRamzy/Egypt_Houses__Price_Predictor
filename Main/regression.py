import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

dataset = pd.read_csv('Main\propertiesUpdated.csv')
X = dataset.iloc[:, :-1].values
y = dataset.iloc[:, -1].values


from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder
ct = ColumnTransformer(transformers=[('encoder', OneHotEncoder(), [0 , 1])], remainder='passthrough')
X = np.array(ct.fit_transform(X))

print(X)