

def numbers():
	filename = "numbers.txt"
	f = open(filename, 'r')
	txt = f.read()
	print(txt.replace(",","\n"))
	
	f.close

if __name__ == '__main__':
	numbers()