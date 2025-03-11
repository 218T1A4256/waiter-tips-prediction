import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

# Load the dataset
data = pd.read_csv("tips.csv")

# Data overview
print(data.head())
print(data.info())
print(data.describe())

# Handling missing values
print(data.isnull().sum())

# Data Visualization
sns.pairplot(data, hue='tip')
plt.show()

# Boxplot for data distribution
data.boxplot(figsize=(15, 6))
plt.show()

# Scatter plot for total bill vs tips with other factors
figure = px.scatter(data, x="total_bill", y="tip", size="size", color="day", trendline="ols")
figure.show()

figure = px.scatter(data, x="total_bill", y="tip", size="size", color="sex", trendline="ols")
figure.show()

figure = px.scatter(data, x="total_bill", y="tip", size="size", color="time", trendline="ols")
figure.show()

# Pie charts for categorical insights
figure = px.pie(data, values='tip', names='day', hole=0.5)
figure.show()

figure = px.pie(data, values='tip', names='sex', hole=0.5)
figure.show()

figure = px.pie(data, values='tip', names='smoker', hole=0.5)
figure.show()

figure = px.pie(data, values='tip', names='time', hole=0.5)
figure.show()

# Data transformation for model training
data["sex"] = data["sex"].map({"Female": 0, "Male": 1})
data["smoker"] = data["smoker"].map({"No": 0, "Yes": 1})
data["day"] = data["day"].map({"Thur": 0, "Fri": 1, "Sat": 2, "Sun": 3})
data["time"] = data["time"].map({"Lunch": 0, "Dinner": 1})

# Correlation heatmap
sns.heatmap(data.corr(), cmap='YlGnBu', annot=True)
plt.show()

# Data preparation
X = np.array(data[["total_bill", "sex", "smoker", "day", "time", "size"]])
y = np.array(data["tip"])

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Model training
model = LinearRegression()
model.fit(X_train, y_train)

# Prediction example
features = np.array([[24.50, 1, 0, 0, 1, 4]])
print("Predicted Tip:", model.predict(features))