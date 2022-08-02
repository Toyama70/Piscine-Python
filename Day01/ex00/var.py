
def	my_var():

	myList = [42, "42", "quarante-deux", 42.0, True, [42], {42: 42}, (42,), set()]

	for x in myList:
		print(x, "has a type ", type(x))


if __name__ == "__main__":
	my_var()
