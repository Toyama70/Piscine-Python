def ft_printer(myList):
	for x in myList:
		print(x[0])

def	ft_resort(myList):
	i = 0
	while(myList[i] and i < len(myList) - 1):
		if ((myList[i][1] == myList[i+1][1]) and myList[i][0] > myList[i+1][0]):
			myList[i], myList[i+1] = myList[i+1], myList[i]
			i = 0
		i += 1
	ft_printer(myList)


def	ft_sort():
	d={
	'Hendrix' : '1942', 
	'Allman' : '1946',
	'King' : '1925', 
	'Clapton' : '1945',
	'Johnson' : '1911', 
	'Berry' : '1926',
	'Vaughan' : '1954', 
	'Page' : '1944', 
	'Richards' : '1943',
	'Hammett' : '1962', 
	'Cobain' : '1967',
	'Garcia' : '1942', 
	'Beck' : '1944', 
	'Santana' : '1947',
	'Cooder' : '1947',
	'Ramone' : '1948', 
	'White' : '1975',
	'Frusciante': '1970', 
	'Thompson' : '1949',
	'Burton' : '1939', }
	myList = sorted(d.items(), key=lambda x: x[1])
	ft_resort(myList)

def	main():
	ft_sort()

if __name__ == '__main__':
	main()