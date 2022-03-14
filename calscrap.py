from bs4 import BeautifulSoup
from numpy import double
import requests
import matplotlib.pyplot as plt
import numpy as np

soup = BeautifulSoup(requests.get('http://www.laalmanac.com/weather/we13.php').content,'html.parser')

# Value that are taken from the website
values = []
#data to be used in the graph
data = {}
# Gets all the data from the table
for x in soup.find_all('td'):
    values.append(x)
#stores the data by year into a hashmap / dictionary stores it as a string
for x in range(len(values)):
    if(x % 3 == 0):
        data[str(values[x-1].string)] = ((values[x].string))
#deleting left over data
del data['+6.59']
for x in data:
    if data[x] == None:
        data[x] = 0.0
    data[x] = float(str(data[x]))

# plotting the years from 1887 and onwards. This x value is 0 to the length of the graph. 
# Cannot use strings due to the fact that it does calculations based on the size of the graph.
# If string is used then it just outputs all of the strings which leads to x axis bloatage
plt.plot([ x + 1877 for x in range(len(data))],[data[x] for x in data])
plt.ylabel("California Rain Graph")
plt.show()
