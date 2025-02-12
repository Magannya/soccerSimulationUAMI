# LOS METODOS EN ESTE ARCHIVO ESTAN PENSADOS PARA EXTRAER INFORMACION
# COMO EL SERVIDOR RESPONDE CON strings, DEFINIMOS FUNCIONES PARA
# REALIZAR ACCIONES ESPECIFICAS CON ESAS CADENAS


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
	
	print(f"s1: <{s1}>, s2: <{s2}>, index: {index}")
	while s2[index] != " ":
		subS += s2[index]
		index += 1
		# PARCHE TEMPORAL EN RESPUESTA A 
		# while s2[index] != " ":
        # IndexError: string index out of range
		if index > len(s2):
			break
			
	return subS
	
# REGRESA LA SUB CADENA DE s QUE ESTA DESPUES DEL ESPACIO ESPECIFICADO
# POR LA VARIABLE spaceIndex
def subStrToSpace(s, spaceIndex):
	out = ""
	index = 0
	
	for c in s:
		
		if c == ' ':
			index += 1
			continue
		if index > spaceIndex:
			break
		else:
			if index == spaceIndex:
				out += c
	
	if len(out) == 0:
		return None
	else:
		return out
		

def subStrFirstFloat(s):
	out = ""
	seccond = False
	first = False
	
	if s[0] == '-':
		first = True
			
	for c in s:
		
		if first:
			out += c
			first = False
			continue
			
		else:
		
			if c == '-':
				seccond = True
			
			if not seccond:
				out += c
		
		if seccond:
			break
		
	return out

