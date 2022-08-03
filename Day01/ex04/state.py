import sys

def	ft_output(position, contents):
	key_list = list(contents[0].keys())
	print(key_list[position])

def	ft_checker(s1, contents):
	if s1 in contents[1].values():
		key_list = list(contents[1].keys())
		val_list = list(contents[1].values())
		position = val_list.index(s1)
		ft_output(position, contents)
	else:
		print("Unknown capital city")

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