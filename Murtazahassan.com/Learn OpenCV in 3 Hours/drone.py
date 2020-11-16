import time
import numpy as np
import sys

# Delay printing
def delay_print(s):
	for c in s:
		sys.stdout.write(c)
		sys.stdout.flush()
		time.sleep(0.05)


# Class
class Pokemon:
	def __init__(self, name, types, moves, EVs, health='=================================================='):
		# Save variables as attributes
		self.name = name
		self.types = types
		self.moves = moves
		self.attack = EVs['ATTACK']
		self.defense = EVs['DEFENSE']
		self.health = health
		self.bars = 50 # Amount of health bars

	def fight(self, Pokemon2):
		print("----- POKEMON BATTLE -----")
		print("\n{}".format(self.name))
		print("TYPE/", self.types)
		print("ATTACK/", self.attack)
		print("DEFENSE/", self.defense)
		print("LVL/", 3*(1+np.mean([self.attack, self.defense])))
		print("\nVS")
	
		print("\n{}".format(Pokemon2.name))
		print("TYPE/", Pokemon2.types)
		print("ATTACK/", Pokemon2.attack)
		print("DEFENSE/", Pokemon2.defense)
		print("LVL/", 3*(1+np.mean([Pokemon2.attack, Pokemon2.defense])))
		print("\n")
		
		time.sleep(2)

		# Consider Weakness and Resistance
		version = ['Fogo', 'Agua', 'Planta']
		for i,k in enumerate(version):
			if self.types == k:
				# Both are the same type
				if Pokemon2.types == k:
					string_1_attack = '\nIts not very effective...'
					string_2_attack = '\nIts not very effective...'
				# Pokemon2 is stronger
				if Pokemon2.types == version[(i+1)%3]:
					Pokemon2.attack *= 2
					Pokemon2.defense *= 2
					self.attack /= 2
					self.defense /= 2
					string_1_attack = '\nIts not very effective...'
					string_2_attack = '\nIts super effective!'
				# Pokemon2 is weaker
				if Pokemon2.types == version[(i+2)%3]:	
					self.attack *= 2
					self.defense *= 2
					Pokemon2.attack /= 2
					Pokemon2.defense /= 2
					string_1_attack = '\nIts super effective!'
					string_2_attack = '\nIts not very effective...'
		
		print("{}\t\tHLTH\t{}".format(self.name, self.health))
		print("{}\t\tHLTH\t{}".format(Pokemon2.name, Pokemon2.health))			
		while self.bars > 0 and Pokemon2.bars > 0:
			print("\nGo {}!".format(self.name))
			for i, x in enumerate(self.moves):
				print("{}.".format(i+1), x)
			index = int(input('Pick a move: '))
			delay_print("{} used {}!".format(self.name, self.moves[index-1]))
			time.sleep(1)
			delay_print(string_1_attack)

			# Determine the damage
			Pokemon2.bars -= self.attack
			Pokemon2.health = ""

			# Add back bars plus defense boost
			for j in range(int(Pokemon2.bars+.1*Pokemon2.defense)):
				Pokemon2.health += "="

			time.sleep(1)
			print("\n{}\t\tHLTH\t{}".format(self.name, self.health))
			print("{}\t\tHLTH\t{}\n".format(Pokemon2.name, Pokemon2.health))
			time.sleep(.5)

			# Check if Pokemon is fainted
			if Pokemon2.bars <= 0:
				delay_print("\n..." + Pokemon2.name + ' fainted.')
				break

			# Pokemon2 Turn


			print("\nGo {}!".format(Pokemon2.name))
			for i, x in enumerate(Pokemon2.moves):
				print("{}.".format(i+1), x)
			index = int(input('Pick a move: '))
			delay_print("{} used {}!".format(Pokemon2.name, Pokemon2.moves[index-1]))
			time.sleep(1)
			delay_print(string_2_attack)

			# Determine the damage
			self.bars -= Pokemon2.attack
			self.health = ""

			# Add back bars plus defense boost
			for j in range(int(Pokemon2.bars+.1*Pokemon2.defense)):
				self.health += "="

			time.sleep(1)
			print("\n{}\t\tHLTH\t{}".format(self.name, self.health))
			print("{}\t\tHLTH\t{}".format(Pokemon2.name, Pokemon2.health))
			time.sleep(.5)

			# Check if Pokemon is fainted
			if self.bars <= 0:
				delay_print("\n..." + self.name + ' fainted.')
				break

			# Pokemon1 Turn

		money = np.random.choice(5000)
		delay_print("\nOpponent paid you ${}.".format(money))
				


if __name__ == '__main__':
	# Create Pokemon
	Charizard = Pokemon('Charizard', 'Fogo', ['Flamethrower', 'Fly', 'Blast Burn', 'Fire Punch'], {'ATTACK':12, 'DEFENSE':8})
	Blastoise = Pokemon('Blastoise', 'Agua', ['Water Gun', 'Bubblebeam', 'Hydro Pump', 'Surf'], {'ATTACK':10, 'DEFENSE':10})		
	Venusaur = Pokemon('Venusaur', 'Planta', ['Vine Wip', 'Razor Leaf', 'Earth Quake', 'Frenzy Plant'], {'ATTACK':8, 'DEFENSE':12})
	
	Charizard.fight(Blastoise)
