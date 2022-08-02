def ft_printer(myDict):
	for key, val in myDict.items():
		print(key, " : ", val)

def switcher(d):
	thisDict = dict()
	i = 0
	while (i < len(d)):
		#print(d[i][1], d[i][0])
		thisDict[d[i][1]] = d[i][0]
		i = i + 1
	ft_printer(thisDict)


def varToDict():
	d = [
		('Hendrix'      , '1942'),
		('Allman'       , '1946'),
		('King'         , '1925'),
		('Clapton'      , '1945'),
		('Johnson'      , '1911'),
		('Berry'        , '1926'),
		('Vaughan'      , '1954'),
		('Cooder'       , '1947'),
		('Page'         , '1944'),
		('Richards'     , '1943'),
		('Hammett'      , '1962'),
		('Cobain'       , '1967'),
		('Garcia'       , '1942'),
		('Beck'         , '1944'),
		('Santana'      , '1947'),
		('Ramone'       , '1948'),
		('White'        , '1975'),
		('Frusciante'   , '1970'),
		('Thompson'     , '1949'),
		('Burton'       , '1939')
	]
	myDict = switcher(d)


if __name__ == '__main__':
	varToDict()
