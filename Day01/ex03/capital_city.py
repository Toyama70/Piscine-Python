import sys

def	ft_checker(s1, contents):
	if s1 in contents[0].keys():
		#I know it exists, but how can I get the exact key position efficiently ?
		st = contents[0].keys()
		print(st)

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
	if (argc != 1):
		sys.exit(1)
	else :
		s1 = sys.argv[1]
	contents = ft_fitting()
	ft_checker(s1, contents)

if __name__ == '__main__':
	ft_main()
	
	#ft_recon