a = 1
b = 1
# we need to circulate several times
for i in range (0,6):
    c = a
    a = c + b
    b = b + a
    print(a,b)

#233 is the target number.
