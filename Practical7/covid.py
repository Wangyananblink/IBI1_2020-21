import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
os.chdir("C:/Users/Lenovo/PycharmProjects/IBI2021317/")
os.getcwd()
os.listdir()
#import .csv
covid_data = pd.read_csv("C:/Users/Lenovo/PycharmProjects/IBI2021317/full_data.csv")
print(covid_data.head(5))
#here we get the median and mean about the new cases
print(covid_data.describe())

# show all columns and the every second row between 0-10
print(covid_data.iloc[0:10:2,])


print(covid_data.iloc[2,0:5])
print(covid_data.iloc[0:2,:])
print(covid_data.iloc[0:10:2,0:5])
print(covid_data.iloc[0:3,[0,1,3]])
selectresult = []
##uese boolean to show something about Afghanistan
for i in range (7996):
    if covid_data.loc[i, "location"] == 'Afghanistan':
        selectresult.append(True)
    else:
        selectresult.append(False)
#we need to select the total cases in the world using the list
nametotal=[False, False, False, False, True, False]
print(covid_data.loc[selectresult,nametotal])
selectworld = []

# for loop is used to select one by one and add the result into the list
for i in range (7996):
    if covid_data.loc[i, "location"] == 'World':
        selectworld.append(True)
    else:
        selectworld.append(False)
#we need to select the new cases in the world using the list
nametotal1=[False, False, True, False, False, False]
print(covid_data.loc[selectworld,nametotal1])
worldnewcase_data = covid_data.loc[selectworld,nametotal1]
#If we want to use. describe(), we need to let the data to be the object, instead of a list containing True and False
print(worldnewcase_data.describe())
# a box plot about newcases
#we need to make a boxplot describing new cases around the World. Since we have got the list of world new cases, we just need to use the command about boxplot.
plt.boxplot(worldnewcase_data)
plt.show()




#plot the data over time: new cases
firstcolumn=[True, False, False, False, False, False]
world_data = covid_data[covid_data["location"] == "World"]
world_dates = world_data.iloc[:,firstcolumn]
x = np.array(world_dates.values.T)
x = x[0]
nametotal1= [False, False, True, False, False, False]
y = np.array(worldnewcase_data.values.T)
plt.xlabel('dates')
y = y[0]
plt.ylabel('new_cases')
plt.xticks(rotation=-90)
plt.plot(x, y, 'b+')
plt.show()

#world new death
nametotal2= [False, False, False, True, False, False]
print(covid_data.loc[selectworld,nametotal2])
worldnewdeath_data = covid_data.loc[selectworld,nametotal2]
firstcolumn=[True, False, False, False, False, False]
world_data = covid_data[covid_data["location"] == "World"]
world_dates = world_data.iloc[:,firstcolumn]
x = np.array(world_dates.values.T)
x = x[0]
nametotal2= [False, False, False, True, False, False]
y = np.array(worldnewdeath_data.values.T)
plt.xlabel('dates')
y = y[0]
plt.ylabel('new_death')
plt.xticks(rotation=-90)
plt.plot(x, y, 'b+')
plt.show()




#the question: how the new cases and total cases changed in China

#different from using the list, it is found that this way is also useful to select location
China_data = covid_data[covid_data["location"] == "China"]
secondcolumn = [False, False, True, False, False, False]
nametotal1= [False, False, False, False, True, False]
firstcolumn = [True, False, False, False, False, False]
China_new_cases = China_data.iloc[:,secondcolumn]
China_total_cases = China_data.iloc[:,nametotal1]
China_dates = China_data.iloc[:,firstcolumn]
#similar with the formal step  the red line and blue line shows total cases and new cases
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
plt.show()










