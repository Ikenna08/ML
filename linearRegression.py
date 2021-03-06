import matplotlib.pyplot as plt
import numpy as np
from sklearn import datasets, linear_model

diabetes = datasets.load_diabetes()
diabetes_X = diabetes.data[:, np.newaxis, 2]
diabetes_X_train = diabetes_X[:-20]
diabetes_X_test = diabetes_X[-20:]
diabetes_y_train = diabetes.target[:-20]
diabetes_y_test = diabetes.target[-20:]
regr = linear_model.LinearRegression()
regr.fit(diabetes_X_train, diabetes_y_train)
print('Coefficients: \n', regr.coef_)
print("Mean squared error: %.2f"
      % np.mean((regr.predict(diabetes_X_test) - diabetes_y_test) ** 2))
print('Variance score: %.2f' % regr.score(diabetes_X_test, diabetes_y_test))
plt.scatter(diabetes_X_test,  diabetes_y_test,  color='green', label="Test")
plt.scatter(diabetes_X_train,  diabetes_y_train,  color='red', label ='Training')
plt.plot(diabetes_X_test, regr.predict(diabetes_X_test), color='blue',
     linewidth=3, label='Best fit line')
plt.xticks(())
plt.yticks(())
plt.legend()

plt.show()