import pandas as pd
import numpy as np
from numpy.linalg import inv
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

df = pd.read_csv('WorldHappiness-2019.csv')
data = df.values
row, col = data.shape
print('\nLoaded Pandas dataframe\n----------\n',df.head())
print('\nExtraxt data (first 5) \n----------\n',data[0:5])

data2 = data[:,1:col] 
print('\nExtraxt data (first 5) \n----------\n',data2[0:5])

data3 = data2[:,0:6]
target = data2[:,6]

X_train, X_test, y_train, y_test = train_test_split(data3, target,
                                        test_size=0.3, random_state=0)

model = LinearRegression()

model.fit(X_train, y_train)

print( '\nmodel coefficient\n----------\n', model.coef_ )
print( '\nmodel intercept\n----------\n', model.intercept_ )

X_test[0] = np.array([1.34, 1.587, 0.986,0.596,0.153,0.393])
y_pred = model.predict(X_test)
print('\n 1st test data\n----------\n', X_test[0])
print('\n1st predicted value\n----------\n', y_pred[0])

y_pred = model.predict(X_test)
plt.plot(y_test, y_pred, '.')
plt.xlabel('actual value')
plt.ylabel('predicted value')
x = np.linspace(3, 8, 5)
y = x
plt.plot(x, y)
plt.show()
