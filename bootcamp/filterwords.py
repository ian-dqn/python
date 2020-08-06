import sys, string

def custom_split(st, size):
	new_string = []
	tmp = ""
	if size == 0:
		return
	for let in st:
		if let == " ":
			if len(tmp) > size:
				new_string.append(tmp)
			tmp = ""
		elif let not in string.punctuation:
			tmp += let
	if len(tmp) > size:
		new_string.append(tmp)
	return new_string
"""
def filter(string, size):

	new_list = []
	i = 0
	tmp = string.split()
	for word in tmp:
		if i < size:
			new_list.append(word)
			i += 1
		else:
			break
	return new_list
"""
if __name__ == '__main__':
	if len(sys.argv) == 3 and sys.argv[2].isnumeric():
		s = custom_split(sys.argv[1], int(sys.argv[2]))
		print(s)
	else:
		print('ERROR')
