gene_lengths=[9410,394141,4442,105338,19149,76779,126550,36296,842,15981]
exon_counts=[51,1142,42,216,25,650,32533,57,1,523]
P = []#we need to create a loop to calculate this for several times.Here,I discussed with Chentao Li
for i in range(len(exon_counts)):
    m = (gene_lengths[i]/exon_counts[i])
    P.append(m)#WE NEED TO ADD NUMBERS TO THE LIST
print(P)


