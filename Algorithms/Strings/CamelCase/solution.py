def camelcase(s):
	count = 0
	for i in range(len(s)-1):
		if s[i+1].isupper():
			count += 1

	return count

if __name__ == '__main__':
    s = 'saveChangesInTheEditor'
    result = camelcase(s)