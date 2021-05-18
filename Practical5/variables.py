a = 20102
b = 190784
c = 100321
d = abs(a-c)
e = abs(a-b)
if d>e:
    print("d>e")
else:
    print("d<=e")

#Use blooean
X = True
Y = False
Z = (X and not Y) or (Y and not X)
if Z == True:
    print("Ture")
else:
    print("False")

W = (X!=Y)
if Z == W:
    print("Z == W")
else:
    print("Z !=W")
