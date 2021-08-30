def superReducedString(s) -> str:
	new = ""
	for i in range(len(s)-1):
		if s[i] != s[i+1]:
			new += s[i]
			
	return s, new

if __name__ == '__main__':
    s = 'aaabccddd'
	
    result = superReducedString(s) 

print(result)