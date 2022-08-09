

def	main():
	dit = {'a':57, 'b':42}
	str = "{a} divise par {b}"
	print(str.format_map(dit))

if __name__ == "__main__":
	main()