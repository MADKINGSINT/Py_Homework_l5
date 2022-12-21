def kodirovka(s):

	kod = "" 

	i = 0
	while i < len(s):
		count = 1

		while i + 1 < len(s) and s[i] == s[i + 1]:
			count = count + 1
			i = i + 1

		kod += str(count) + s[i]
		i = i + 1

	return kod


if __name__ == '__main__':

	s = 'ABBCCCDBBBBBBBBBjnjjjBBBBBBBBBBBYYYYYYYYYYYYYYYYYYYYYYYYYYYYDDDDDLLLLLLLLLLLLLLLL'
	print(kodirovka(s))