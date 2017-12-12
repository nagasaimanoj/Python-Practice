from csv import reader
from matplotlib import pyplot
from numpy import array

csv_file = open("C:\\Users\\saimanoj\\Downloads\\revenue.csv")
csv_reader = reader(csv_file)
csv_data = array(list(csv_reader))

x_data = csv_data[..., 0]
y_data = csv_data[..., 1]

pyplot.plot(x_data, y_data, marker='o')

pyplot.show()
