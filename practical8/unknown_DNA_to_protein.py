import sys
import os
import re


#We use the code wrote before
def codep(seq):
    animoacid = ''
    for i in range(0, len(seq), 3):
        animoacid += code[seq[i:i + 3]]
    return animoacid


os.chdir("C:/Users/Lenovo/Documents/GitHub/IBI1_2020-21/practical8")
# Build up a divtionary
code = {
    "TTT": 'F', "TTC": 'F', "TTA": 'L', "TTG": 'L',
    "TCT": 'S', "TCC": 'S', "TCA": 'S', "TCG": 'S',
    "TAT": 'Y', "TAC": 'Y', "TAA": 'O', "TAG": 'U',
    "TGT": 'C', "TGC": 'C', "TGA": 'X', "TGG": 'W',
    "CTT": 'L', "CTC": 'L', "CTA": 'L', "CTG": 'L',
    "CCT": 'P', "CCC": 'P', "CCA": 'P', "CCG": 'P',
    "CAT": 'H', "CAC": 'H', "CAA": 'Q', "CAG": 'Z',
    "CGT": 'R', "CGC": 'R', "CGA": 'R', "CGG": 'R',
    "ATT": 'I', "ATC": 'I', "ATA": 'J', "ATG": 'M',
    "ACT": 'T', "ACC": 'T', "ACA": 'T', "ACG": 'T',
    "AAT": 'N', "AAC": 'B', "AAA": 'K', "AAG": 'K',
    "AGT": 'S', "AGC": 'S', "AGA": 'R', "AGG": 'R',
    "GTT": 'V', "GTC": 'V', "GTA": 'V', "GTG": 'V',
    "GCT": 'A', "GCC": 'A', "GCA": 'A', "GCG": 'A',
    "GAT": 'D', "GAC": 'D', "GAA": 'E', "GAG": 'E',
    "GGT": 'G', "GGC": 'G', "GGA": 'G', "GGG": 'G',
}

name = "peptide.unknown.fa"
# input files and open output file
file1 = open('unknown_function.fa', 'r')
file2 = open(name, 'w')

line = next(file1, '0')
while True:
    if line.startswith('>>'):
        first = line#This is the first line of each gene/DNA

        line = next(file1, '0')# The 'next' is used to run the lines one by one
        sequence = line.replace('\n', '')

        information = first[0:18] + str(int(len(s) / 3))#This part illustrate the realated information and its sequence length
        file2.write(information+'\n'+codep(sequence)+'\n')
        #We use.write to write the result in the file.

    if line == '0':  #We use this code to end the program
        break
    line = next(file1, '0')
# We use .open, so we use.close here.
file1.close()
file2.close()