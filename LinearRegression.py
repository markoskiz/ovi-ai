import numpy as np
from sklearn import datasets, linear_model
from sklearn.metrics import mean_squared_error, r2_score
import matplotlib.pyplot as plt

# Code source: Jaques Grobler
# License: BSD 3 clause

# Load the diabetes dataset
diabetes = datasets.load_diabetes()

# Use only one feature
diabetes_x = diabetes.data[:, np.newaxis, 2]
print(diabetes.data[:3])

# Split the data into training/testing sets
diabetes_x_train = diabetes_x[:-20]
diabetes_x_test = diabetes_x[-20:]

print(diabetes_x_train[:3])
print(diabetes_x_test.shape)

# Split the targets into training/testing sets
diabetes_y_train = diabetes.target[:-20]
diabetes_y_test = diabetes.target[-20:]

print(diabetes_y_train.shape)
print(diabetes_y_test.shape)
# Create linear regression object
regression_model = linear_model.LinearRegression()

# Train the model using the training sets
regression_model.fit(diabetes_x_train, diabetes_y_train)

# Make predictions using the testing set
diabetes_y_pred = regression_model.predict(diabetes_x_test)

# The coefficients
print('Coefficients: \n', regression_model.coef_)
# The mean squared error
print("Mean squared error:", mean_squared_error(diabetes_y_test, diabetes_y_pred))

# Plot outputs
plt.scatter(diabetes_x_test, diabetes_y_test,  color='black')
plt.plot(diabetes_x_test, diabetes_y_pred, color='blue', linewidth=3)
print(diabetes_y_test)
plt.title('Регресија')
plt.show()
