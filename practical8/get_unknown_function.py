import re
original_file = open('Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa', 'r')
new_file = open('unknown_function.fa','w')
for line in original_file:
    if line.startswith('>') and re.search('unknown function',line):
        name = re.findall(r'gene:(\S+)',line)#There is only one name in this line, so the result of re.findall is suitable.
        real_name = ''.join(name)  #output a str
        gene = ''
        while True:
            line = next(original_file) #get to the next line, I learnt this from my classmate Ye liyuan.
            if not line.startswith('>'):
                gene += line.replace('\n', '')
            else:
                break
        length = str(int(len(gene)))
        new_file.write('>>'+real_name+'              '+length+'\n'+gene+'\n')#\n was used to make the result more clear
original_file.close()
