import random
from beverages import *

class CoffeeMachine():
	def __init__(self):
		self.Obsolescence = 0
		print("A wild coffee machine appeared.")

	def __del__(self):
		print("A wild coffee machine disappeared.")

	class EmptyCup(HotBeverage):
		name = "empty cup"
		price = 0.90

		def	description(self):
			return ("An empty cup?! Gimme my money back!")

	class BrokenMachineException(Exception):
		def __init__(self, message="This coffee machine has to be repaired"):
			self.message = message
			super().__init__(self.message)
			raise Exception(self.message)

	def	repair(self):
		self.Obsolescence = 0

	def	serve(self, HotDrink):
		
		if (self.Obsolescence == 10):
			return self.BrokenMachineException()
		self.Obsolescence += 1
		if (random.randint(0,9) % 2) == 0:
			HotDrink.__str__()
			return HotDrink
		else:
			garbage = self.EmptyCup()
			garbage.__str__() 
			return garbage


#Need to watch fully Exception video