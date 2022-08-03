import sys

def	ft_output(keyOrValue, position, onlyNames):
	if (keyOrValue == 1):
		print(onlyNames[1][position], "is the capital of", onlyNames[0][position])

def	ft_checker(s1, contents):
	key_list_state = list(contents[0].keys())
	val_list_capital = list(contents[1].values())
	onlyNames = []
	onlyNames.append(key_list_state)
	onlyNames.append(val_list_capital)
	
	key_lower = [x.lower() for x in key_list_state]
	val_lower = [x.lower() for x in val_list_capital]
	s1_lower = [x.lower() for x in s1]
	for k in s1_lower:
		if k in key_lower:
			position = key_lower.index(k)
			ft_output(1, position, onlyNames)
		elif k in val_lower:
			position = val_lower.index(k)
			ft_output(1, position, onlyNames)
		else: print(k, "is neither a capital city nor a state")

def	ft_fitting():
	states = {
	"Oregon" : "OR", 
	"Alabama" : "AL",
	"New Jersey": "NJ",
	"Colorado" : "CO"
	}
	capital_cities = {
	  "OR": "Salem",
	"AL": "Montgomery",
	"NJ": "Trenton",
	"CO": "Denver"
	}
	contents = [states]
	contents.append(capital_cities)
	return contents

def	ft_splitter(s1):
	s1 = s1.split(",")
	s1 = [x.strip() for x in s1]
	return (s1)

def	allSpace(string):
	n = len(string)
	if (n == 0):
		return(True)
	else: return(False)

def	ft_main():
	argc = len(sys.argv) - 1
	if (argc != 1):
		sys.exit(1)
	else :
			s1 = sys.argv[1]
	if (s1.find(",,") != -1):
		sys.exit(1)
	s1 = ft_splitter(s1)
	for x in s1:
		if allSpace(x) is True:
			sys.exit(1)
	contents = ft_fitting()
	ft_checker(s1, contents)



if __name__ == '__main__':
	ft_main()