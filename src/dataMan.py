def strDiff2(s1, s2):
	if len(s1) > len(s2):
		aux = s2
		s2 = s1
		s1 = aux
	out = ""
	for c in s2:
		if c not in s1:
			out += c
	
	out2 = ""
	index = 1
	while index < len(out):
		out2 += out[index]
		index += 1
		
	#print (f"s1: ->{s1}<- s2: ->{s2}<- out2: ->{out2}<-")
	return out2

def strDiff(s1, s2):
	if len(s1) > len(s2):
		aux = s2
		s2 = s1
		s1 = aux
	out = ""
	index = len(s1) + 1
	while index < len(s2):
		out += s2[index]
		index += 1
		
	#print(f"<{out}>")
	return out
	
# RECIBE DOS CADENAS Y TE REGRESA LA SUBCADENA DESDE QUE TERMINA
# LA CADENA 1 HASTA QUE ENCUENTRA UN ESPACIO EN BLANCO

def subStrToNextWhite(s1, s2):
	
	if len(s1) > len(s2):
		aux = s1
		s1 = s2
		s2 = aux
		print(True)
	
	index = s2.find(s1) + len(s1) + 1
	subS = ""
	while s2[index] != " ":
		subS += s2[index]
		index += 1
	return subS
	
# REGRESA LA SUBCADENA DE s HASTA QUE ENCUENTRA UN ESPACIO EN BLANCO
# SI NO HAY UNA ESPACIO, REGRESA LA CADENA COMPLETA	
def subStrToSpace(s, spaceIndex):
	out = ""
	index = 0
	
	for c in s:
		
		if index > spaceIndex:
			break
		
		if index == spaceIndex:
			if c == ' ':
				index += 1
			else:
				out += c
					
	return out

