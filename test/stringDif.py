def strDif(a, b):
	s3 = ""
	if a in b:
		index = len(a) + 1
		while index < len(b):
			s3 += b[index]
			index += 1
		return s3
	else:
		print(f"{a} is not in {b}")
		return None
if __name__ == "__main__":
	s1 = "stamina"
	s2 = "stamina 8000 0"
	print(strDif(s1, s2))
