import sys

def	ft_checker(s1, contents):
	if s1 in contents[0].keys():
		found = contents[0][s1]
		print(contents[1][found])
	else:
		print("Unknown state")

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


def	ft_main():
	argc = len(sys.argv) - 1
	if (argc != 1 and (sys.argv[1] != "New" and sys.argv[2] != "Jersey")):
		sys.exit(1)
	else :
		if (argc == 2):
			s1 = sys.argv[1] + " " + sys.argv[2]
		else : 
			s1 = sys.argv[1]
	contents = ft_fitting()
	ft_checker(s1, contents)

if __name__ == '__main__':
	ft_main()