import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
os.chdir("C:/Users/Lenovo/PycharmProjects/IBI2021317")
covid_data = pd.read_csv("full_data.csv")

print(covid_data.iloc[0:12:2,:]) # Show all columns, and every second row between (and including) 0 and 10.

row_number = len(covid_data)
for i in range(0,row_number):
     #In if statement, the boolean was used to evaluate whether the location is Afghanistan
     if covid_data.loc[i,"location"] == "Afghanistan":
         print(covid_data.loc[i, "total_cases"])

world_new_cases = []#The list was used to store the statistics.
world_dates = []
new_death_worldwide = []
for i in range(0,row_number):
    if covid_data.loc[i,"location"] == "World":
        world_new_cases.append(covid_data.loc[i,"new_cases"])
        world_dates.append(covid_data.loc[i,"date"])
        new_death_worldwide.append(covid_data.loc[i,"new_deaths"])
n = len(world_new_cases)
a = np.array(world_new_cases) # Using the numpy imported before
mean = np.mean(a)
print("Mean for new cases around the world: " + str(mean))
median = np.median(world_new_cases)#We use the .median in numpy to get the median value directly
Median = np.median(a)
print("Median for new cases around the world: " + str(Median))

plt.boxplot(world_new_cases, showmeans= True)
plt.title('The new cases around the World')#illustrate the tittle
plt.show()

plt.plot(world_dates, world_new_cases, 'b', label = "World new cases")#In this way, we allow a plot containing both new cases and new deaths
plt.plot(world_dates, new_death_worldwide, 'r', label = "World new deaths")
plt.xlabel("Date")
plt.ylabel("Number of people")
plt.title("New cases and new deaths worldwide")
plt.legend()
plt.xticks(covid_data.date.iloc[0:len(covid_data.date):960], rotation=-90, fontsize=8)

plt.show()
# the question: how the new cases and total cases changed in China
#In this question, we use boolean to get statistics.


# different from using the list, it is found that this way is also useful to select location
China_data = covid_data[covid_data["location"] == "China"]
secondcolumn = [False, False, True, False, False, False]
nametotal1 = [False, False, False, False, True, False]
firstcolumn = [True, False, False, False, False, False]
China_new_cases = China_data.iloc[:, secondcolumn]
China_total_cases = China_data.iloc[:, nametotal1]
China_dates = China_data.iloc[:, firstcolumn]
# The red line and blue line shows total cases and new cases
x = np.array(China_dates.values.T)
x = x[0]
y = np.array(China_new_cases.values.T)
y = y[0]
z = np.array(China_total_cases.values.T)
z = z[0]
plt.xlabel('dates')
plt.ylabel('cases')
plt.xticks(rotation=-90)
plt.plot(x, y, 'c-')
plt.plot(x, z, 'r-')
plt.title('how the new cases and total cases changed in China')
plt.show()
