#This program will cost about ten minutes to run
#In general, this code find the parent nodes related to DNA.
import re
import os
from xml.dom.minidom import parse
import xml.dom.minidom
import matplotlib.pyplot as plt


#We need to run the code for four times, so I use function for convenience.
def findparent(molecule,term):
    allis_a = []
    returnvalue = False
    allis_a=term.getElementsByTagName('is_a')
    if allis_a == []:
        returnvalue = False
    else:
#A single term may contain several is_a elements, so we use for loop
        for everyis_a in allis_a:
            parentID = everyis_a.childNodes[0].data  # To get the text(ID) of its father
            strID = re.findall('(\d.*)', parentID)
            pure_parentID = int(strID[0])  # Change the string to integer, prepare for the 'loc'
            parent_term = terms[loc[pure_parentID]]  # Localize the fatherterm
            parent_defstr = parent_term.getElementsByTagName('defstr')[0].childNodes[0].data  # Move to list containing the only element called 'defster'
            if re.search(molecule, parent_defstr):  # Evaluate the existece of molecule in the defstr part
                returnvalue = True#If we just use return True/return False, we can't get the all result we need.
            elif findparent(molecule, parent_term):
                returnvalue = True
    return returnvalue
os.chdir('C:/Users/Lenovo/Desktop')
go_obo = open('go_obo.xml','r')
DOMTree = xml.dom.minidom.parse('go_obo.xml')
collection = DOMTree.documentElement
terms = collection.getElementsByTagName('term')
number_of_DNA=0
number_of_RNA=0
number_of_protein=0
number_of_oligosaccharide=0
oligocount=0
i=0
loc=[0]*10000000
for term in terms:#This part make the program run more quickly. I learnt this part from my classmate  Li zhekai
    termid = term.getElementsByTagName('id')[0].childNodes[0].data
    p = re.findall('(\d.*)',termid)
    q = int(p[0])
    loc[q] = i
    i = i+1
for term in terms:
    if findparent('DNA',term):
        number_of_DNA += 1

for term in terms:
    if findparent('RNA',term):
        number_of_RNA +=1
#the number of childNodes associated with protein#
for term in terms:
    if findparent('protein',term):
        number_of_protein += 1
#the number of childNodes associated with carbohydrate#
for term in terms:
    if findparent('oligosaccharide',term):
        number_of_oligosaccharide += 1
print('ChildNodes with DNA: ',number_of_DNA)
print('ChildNodes with RNA: ',number_of_RNA)
print('ChildNodes with protein: ',number_of_protein)
print('ChildNodes with oligosaccharide: ',number_of_oligosaccharide)
labels = 'DNA\n'+str(number_of_DNA),'RNA\n'+str(number_of_RNA),'protein\n'+str(number_of_protein),'oligosaccharide\n'+str(number_of_oligosaccharide)
sizes = [number_of_DNA,number_of_RNA,number_of_protein,number_of_oligosaccharide]
plt.pie(sizes, explode=None, labels=labels,
    colors=('b', 'g', 'r', 'c'),
    autopct='%1.2f%%', pctdistance=0.6, shadow=True,
    labeldistance=1.1, startangle=0, radius=1,
    counterclock=True, wedgeprops=None, textprops=None,
    center = (0, 0), frame = False )
plt.title('Child Nodes of Macromolecules')
plt.axis('equal')
plt.show()
