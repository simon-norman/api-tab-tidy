import numpy as numpy
import matplotlib.pyplot as plot
import pandas as pandas
from sklearn.model_selection import train_test_split

tabs_data = pandas.read_csv('/api-tab-tidy/model-generator/test_tabs_data.csv')
x = tabs_data.iloc[:, 1]
y = tabs_data.iloc[:, 0]

X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=0)

