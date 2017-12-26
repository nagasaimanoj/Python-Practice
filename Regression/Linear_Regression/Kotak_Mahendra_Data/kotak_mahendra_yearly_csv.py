import csv

from matplotlib import pyplot as plt
import numpy as np
from sklearn import linear_model

# reading CSV file from local disk
csv_file = open("C:\\Users\\saimanoj\\Downloads\\data.csv")
csv_reader = csv.reader(csv_file)
csv_data = np.array(list(csv_reader))

# taking the needed columns. date & amount
x_data = np.array(csv_data[..., :1], dtype=int)
y_data = np.array(csv_data[..., 1:], dtype=float).T[0]

# creating regression object & training with existing data
regr = linear_model.LinearRegression()
regr.fit(x_data, y_data)

# plotting a graph using existing data
plt.plot(x_data, y_data, marker='o')

# adding 5 years to our date variable to use for predection
x_data = np.array(np.append(x_data, np.arange(
    max(x_data) + 1, max(x_data) + 6)))

# transposing (1, len) array to (len, 1) array
x_data.shape = (len(x_data), 1)

# plotting a graph using predected data
plt.plot(x_data, regr.predict(x_data), marker='o')
plt.show()