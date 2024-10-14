# -*- coding: utf-8 -*-
"""New landslide prediction.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1Zf0JHCvUMfPy8_mUsCiBpIHZaf0w6vvn
"""

from google.colab import drive
drive.mount('/drive')

from google.colab import files
import pandas as pd
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import seaborn as sns
import os

uploaded = files.upload()

# Get the first file name in the uploaded files
file_name = list(uploaded.keys())[0]

# Read the CSV file
data = pd.read_csv(file_name)

# Display the first few rows of the DataFrame
data.head()

current_directory = os.getcwd()

# Specify the file name without a path if it's in the same directory
file_name = "/content/Complete-data (1).csv"

# Create the full file path
file_path = os.path.join(current_directory, file_name)

if os.path.exists(file_path):
    data = pd.read_csv(file_path)
    # Continue with your data processing
else:
    print(f"File not found: {file_path}")

data.head()

data.tail()

data.info

data.describe()

data.shape

data.columns

data.max()

data.min()

data.count()

data.corr()

data.isna()

data['Landslide'].plot()

data['Aspect'].plot()

data['Curvature'].plot()

data['Earthquake'].plot.hist()

data.sort_values(by = "Landslide", ascending = True)

data.sort_values(by = "Landslide", ascending = False)

data.sort_values (by = "Curvature", ascending = False)

data.sort_values(by = "NDVI", ascending = False)

data.max()

data.min()

data['Aspect'].plot.hist()

data['Flow'].unique()
data['Plan'].unique()
data['Slope'].unique()

data['Earthquake'].value_counts()

data.duplicated().sum()

data['Profile'].max()

list1 = ['Aspect', 'Earthquake', 'Flow','Landslide','Slope']
sns.heatmap(data[list1].corr(), annot = True, fmt= '.2f')
plt.show()

g = sns.catplot(x='NDVI', y='NDWI', data=data, kind='bar', height=8)
g.set_ylabels('Landslide prediction Probability')
plt.show()

pivot = pd.pivot_table(data, values = "Slope", index = "Flow", columns = "Landslide", aggfunc = np.mean)
ax = pivot.plot(kind = "bar", alpha = 0.5)
plt.title('Title')
plt.xlabel('X AXIS')
plt.ylabel('Y AXIS')
plt.show()

sns.boxplot(x = "Aspect", y= "Curvature", data = data)

sns.FacetGrid(data, hue="Landslide", height=6) \
   .map(sns.kdeplot, "Plan") \
   .add_legend()

"""# TOP 5 ALGORITHM USED FOR LANDSLIDE PREDICTION

# 1) LOGISTIC REGRESSION ALGORITHM
"""

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix, classification_report

# Loading the landslide dataset
data = pd.read_csv('/content/Complete-data (1).csv')

# Assigning features to X and the target variable to y
X = data.drop('NDVI', axis=1)
y = data['NDWI']

# Splitting the dataset into a training set and a testing set
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Creating a logistic regression model
model = LogisticRegression()

# Training the model
model.fit(X_train, y_train)

# Making predictions on the testing set
y_pred = model.predict(X_test)

# Printing the confusion matrix and the classification report
print("Confusion Matrix:")
print(confusion_matrix(y_test, y_pred))
print("\nClassification Report:")
print(classification_report(y_test, y_pred))

"""# 2) XGBOOST ALGORITHM"""

from xgboost import XGBClassifier
from sklearn.metrics import confusion_matrix, classification_report

data = pd.read_csv('/content/Complete-data (1).csv')

# Assigning features to X and the target variable to y
X = data.drop('NDWI', axis=1)
y = data['NDWI']

# Mapping the 'NDWI' values to the expected classes
y = y.map({1: 0, 2: 1, 3: 2, 4: 3, 5: 4})

# Splitting the dataset into a training set and a testing set
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Creating an XGBoost model
model = XGBClassifier()

# Training the model
model.fit(X_train, y_train)

# Making predictions on the testing set
y_pred = model.predict(X_test)

# Printing the confusion matrix and the classification report
print("Confusion Matrix:")
print(confusion_matrix(y_test, y_pred))
print("\nClassification Report:")
print(classification_report(y_test, y_pred))

"""# 3) DECISION TREES ALGORITHM"""

from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import confusion_matrix, classification_report

data = pd.read_csv('/content/Complete-data (1).csv')

# Assigning features to X and the target variable to y
X = data.drop('NDVI', axis=1)
y = data['NDWI']

# Splitting the dataset into a training set and a testing set
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Creating a decision tree model
model = DecisionTreeClassifier(random_state=42)

# Training the model
model.fit(X_train, y_train)

# Making predictions on the testing set
y_pred = model.predict(X_test)

# Printing the confusion matrix and the classification report
print("Confusion Matrix:")
print(confusion_matrix(y_test, y_pred))
print("\nClassification Report:")
print(classification_report(y_test, y_pred))

"""# 4) SUPPORT VECTOR MACHINE ALGORITHM"""

from sklearn import svm
from sklearn.metrics import confusion_matrix, classification_report

data = pd.read_csv('/content/Complete-data (1).csv')

# Assigning features to X and the target variable to y
X = data.drop('NDVI', axis=1)
y = data['NDWI']

# Splitting the dataset into a training set and a testing set
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Creating an SVM model
model = svm.SVC(kernel='rbf', C=1, gamma=0.1)

# Training the model
model.fit(X_train, y_train)

# Making predictions on the testing set
y_pred = model.predict(X_test)

# Printing the confusion matrix and the classification report
print("Confusion Matrix:")
print(confusion_matrix(y_test, y_pred))
print("\nClassification Report:")
print(classification_report(y_test, y_pred))

"""# 5) NEURAL NETWORK ALGORITHM"""

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense

# Load your dataset (replace 'your_dataset.csv' with your actual file)
df = pd.read_csv('/content/Complete-data.csv')

# Assuming you have columns like 'feature1', 'feature2', ..., 'label'
features = df.drop('NDVI', axis=1).values
labels = df['NDWI'].values

# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(features, labels, test_size=0.2, random_state=42)

# Standardize the features (optional but recommended for neural networks)
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# Build the neural network model
model = Sequential()
model.add(Dense(128, input_dim=X_train.shape[1], activation='relu'))
model.add(Dense(64, activation='relu'))
model.add(Dense(1, activation='sigmoid'))

# Compile the model
model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

# Train the model
model.fit(X_train, y_train, epochs=10, batch_size=32, validation_split=0.2)

# Evaluate the model on the test set
y_pred = (model.predict(X_test) > 0.5).astype(int)
accuracy = accuracy_score(y_test, y_pred)
print(f'Accuracy on the test set: {accuracy}')

# Save the model if needed
model.save('landslide_prediction_model.h5')

