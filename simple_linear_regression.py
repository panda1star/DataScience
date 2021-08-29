# Simple Linear Regression
# Data Preprocessing Template

# Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

#How to see current working directory

dataset = pd.read_csv('water_potability.csv')




#'ph'	'Hardness'	'Solids'	'Chloramines'	'Sulfate'	'Conductivity'	'Organic_carbon'	'Trihalomethanes'	'Turbidity'


X=dataset[['ph','Hardness','Solids','Chloramines','Sulfate','Conductivity','Organic_carbon','Trihalomethanes' ]]
y = dataset['Turbidity']

#from sklearn.preprocessing import Imputer
#imputer = Imputer(missing_values= np.nan, strategy='mean',axis = 0)

#imputer.fit(X.iloc[:, 0:6])
#X[:, 0:6] = imputer.transform(X[:, 0:6])


# =============================================================================
# =============================================================================
  # Splitting the dataset into the Training set and Test set
from sklearn.cross_validation import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 1/3, random_state = 0)
  
 # Fitting Simple Linear Regression to the Training set
from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor.fit(X_train,y_train)
  
  #Predicting the test set results
  
y_perd = regressor.predict(X_test)
  
  #Visualising the training set results
plt.scatter(X_train,y_train,color="red")
plt.plot(X_train[:,0],regressor.predict(X_train), color="blue")
plt.title = "Salary vs Experience(Traing Set)"
plt.xlabel("Years of Experience")
plt.ylabel("Salary")
plt.show()
  
  #Visualising the test set results
plt.scatter(X_test,y_test,color="red")
plt.plot(X_test[:,0],regressor.predict(X_test[:,0]), color= "blue")
plt.title = "Salary vs Experience(Test Set)"
plt.xlabel("Years of Experience")
plt.ylabel("Salary")
plt.show()
  
# =============================================================================
# =============================================================================




























