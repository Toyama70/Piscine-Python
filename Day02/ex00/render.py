from settings import *
import sys

def	ecriture():
	f = open("file.template", 'r')
	content = f.read()
	a_ecrire = content.format_map(globals())
	file_html = "file.template".replace(".template", ".html")
	print(globals())
#	print(content, "\n")
	print(a_ecrire)
#	print(file_html)
	f_h = open(file_html, 'w')
	f_h.write(a_ecrire)

if __name__ == '__main__':
	ecriture()