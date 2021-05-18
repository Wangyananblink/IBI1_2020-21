def reverse(DNAs):

    seq = list(DNAs)
    #Get the complement sequence
    for i in range(len(seq)):
        if (seq[i]=='A')or(seq[i]=='a'):#For each upper form and lower form, we use this kinds of code to get the complement word
            seq[i]='T'
            continue
        if (seq[i]=='C')or(seq[i]=='c'):
            seq[i]='G'
            continue
        if (seq[i]=='G')or(seq[i]=='g'):
            seq[i]='C'
            continue
        if (seq[i]=='T')or(seq[i]=='t'):
            seq[i]='A'
            continue
    base = ''
    #get the reverse one
    for i in range(len(seq)-1,-1,-1): #We use -1 to ensure the result of reverse sequence        
        base = base + str(seq[i])
    print("Reverse complement:",base)
reverse('AGGTTCatgcaat')