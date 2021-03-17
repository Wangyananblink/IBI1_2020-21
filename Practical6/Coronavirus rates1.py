
genes = {'USA':29862124,'India':11285561,'Brazil':11205972,'Russia':4360823,'UK':4234924}
L = [29862124,11285561,11205972,4360823,4234924]#we can not use the dictionary directly in the loop. so we need to create a list for convinence
total = 0
for i in range(len(L)):
    total += L[i]
print(total)
P = []
for k in range(len(L)):
    a = float(L[k]/total)
    P.append(a)
import matplotlib.pyplot as plt#imitate the model in the ppt
labels = 'USA','India','Brazil','Russia','UK'
plt.pie(P, labels=labels, autopct = '%1.1f%%')
plt.axis('equal')
plt.show()
