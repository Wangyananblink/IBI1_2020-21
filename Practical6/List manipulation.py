gene_lengths=[9410,394141,4442,105338,19149,76779,126550,36296,842,15981]
exon_counts=[51,1142,42,216,25,650,32533,57,1,523]
#We need to calculate the average length of exons, so we use a list to store the statistics
ave=[]
for i in range(len(gene_lengths)):
    ave.append(gene_lengths[i]/exon_counts[i])

ave.sort()#Forget to sort the statistic before
print(ave)
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Polygon

fig, axs = plt.subplots()
# basic plot
axs.boxplot(ave)
axs.set_title('The distribution of average exon length')

plt.show()

