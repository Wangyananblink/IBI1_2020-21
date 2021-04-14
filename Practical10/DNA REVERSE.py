seq='AAAcgAGCttTTCgGTTG'
def uppercom(m):
	SEQ=str.upper(m)
	CDNA=''
	for i in range (len(SEQ)):
		if SEQ[i-1]=='A':
			CDNA+='T'
		elif SEQ[i-1]=='G':
			CDNA+='C'
		elif SEQ[i-1]=='C':
			CDNA+='G'
		elif SEQ[i-1]=='T':
			CDNA+='A'
	return (CDNA)
print(uppercom(seq))