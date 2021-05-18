# Import the package first
import matplotlib.pyplot as plt

country = ['USA','India','Brazil','Russia','UK']
cases = [29862124,11285561,11205972,4360823,4234924]
frequency = []
total=0
#Use for loop to calculate total number
for i in range(len(cases)):
    total+=cases[i]
print(total)

# Use for loop to calculate the frequency
for i in range(len(cases)):
    frequency.append(cases[i] / total)

dicfrequency = dict(zip(country,frequency))# Use dict(zip)to combine two lists and get a new dictionary
dic = dict(zip(country,cases))
print(dicfrequency)
#Here we use plt to get the pie chart
plt.pie(dic.values(),labels=dic.keys(),autopct='%1.1f%%',shadow=True,startangle=90)# Learn it from official demo
plt.title('Pie Chart about Frequency of Total Number of Cases for Five Countries')
plt.axis('equal')
plt.show()