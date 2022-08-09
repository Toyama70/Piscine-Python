import sys

def	ft_output():
	str = "<!DOCTYPE html>\n<html>\n<head>\n<title>Periodic table</title>"
	str2 = "</head>\n<body>\n<h1>Periodic table</h1>"
	f = open("periodic_table.html", "w")
	f.write(str)
	f.write(str2)

def	main():
	print("ok")
	ft_output()


if __name__ == '__main__':
	main()