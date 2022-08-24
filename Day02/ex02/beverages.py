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
	test1 = HotBeverage()
	test2 = Coffee()
	test3 = Tea()

	test1.__str__()
	test2.__str__()
	test3.__str__()
