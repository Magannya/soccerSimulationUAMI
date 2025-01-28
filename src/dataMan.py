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
	
