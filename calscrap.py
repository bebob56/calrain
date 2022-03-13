from bs4 import BeautifulSoup
from numpy import double
import requests

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

print(data)