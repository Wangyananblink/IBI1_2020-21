n = 84  # The number of infected people at the first time.
r = 1.2# The number of new infected is calculated using n*r
m = 0#The variable to store the number of newly infected people
for i in range(1, 6):
    m = r * n  # Calculate the newly infected people
    n = m + n  # Calculate the total number of infected people
print("R rate : " + str(r) + "  The total number of individuals infected after 5 generations : " + str(n))
