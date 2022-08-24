from machine import *

class HotBeverage:
	price = 0.30
	name = "hot beverage"

	def	description(self):
		return ("Just some hot water in a cup")

	def __str__(self):
		print("name : " + self.name)
		print("price : " + str(self.price))
		print("description : " + self.description())


class	Coffee(HotBeverage):
	name = "coffee"
	price = 0.40
	def description(self): 
		return ("A coffee, to stay awake")

class	Tea(HotBeverage):
	name = "Tea"

class	Chocolate(HotBeverage):
	name = "chocolate"
	price = 0.50
	def description(self):
		return ("Chocolate, sweet cholotate...")
	
class Cappuccino(HotBeverage):
	name = "cappuccino"
	price = 0.45
	def description(self):
		return ("Un po' di Italia nella sua tazza!")

if __name__ == '__main__':
	test1 = CoffeeMachine()
	boisson = Cappuccino()
	i = 0
	while (i < 12):
		try:
			test1.serve(boisson)
		except Exception as e:
			print(e)
		
		i += 1
		print("\n WE ARE AT TEST N:" + str(i))


"""
	print("Here we go ONE MORE TIME AND REPAIRING FIRST \n")
	test1.repair()

	while (i < 25):
		test1.serve(boisson)
		i += 1
		print("\n WE ARE AT TEST N:" + str(i))"""