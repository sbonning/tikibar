##Sam's Tiki Bar project in the "Pirate Bartender" Assignment for Thinkful
##Mixing delicious tiki drinks since 2017!
##Description of functionality:
## - the Bartender will ask a series of questions about your tastes
## - the Bartender will mix you up a delicious beverage/s until you are done!

def drink_program ():
	"""Ties the entire program together"""
	welcome()

	glass_pref()

	drink_pref()

	drink_mix(drink)

	print ("Here you go!")

def welcome ():
	"""Welcome the customer to the bar"""
	print ("A bartender with one eye greets you with a smile.  Or a grimace.  It's hard to tell.\n")
	print ("	-Welcome to Sam's Tiki Bar!")

def glass_pref ():
	"""I welcome the customer and choose a glass for the drink"""
	glassware = {'1': "cute animal mug", '2': "culturally appropriate mug"}
	print ("	-First choose your glassware.  We pride ourselves on our original Tiki mugs!")
	print ("	-What are you thinking: Novelty animal, or one of our cultural options?\n")
	print ("The bartender shows you a selection of mugs, including a Lucky Cat and a terrifying Fu Man Chu")
	glass = input("If you want one of those cute animals, choose 1.\nFor the cultural option, choose 2.\n")
	while True:
		try:
			glassware[glass]
			break
		except:
			print ("	-I've only got novelty mugs. Sorry!")
			glass = input("If you want one of those cute animals, choose 1.\nFor the cultural option, choose 2.\n")
	# how do I add a space between the two options?
	print ("Great choice. I love a {}.".format(glassware.get(glass)))
	return glass

def drink_pref ():
	"""I gather the input about customer taste preferences"""
	print ("The bartender waves your mug choice at you.\n")
	## later I want to add an input for the mug from the glass_pref
	print ("	-Now I gotta fill this up with something.\n")
	repeat = True
	while repeat == True:
		print ("Choose yes or no for the following questions:\n")
		strong_pref = input("	-Do you like a strong beverage? ") 
		salty_pref = input ("	-How about something a little salty? ")
		bitter_pref = input ("	-Bitter, perhaps? ")
		fruity_pref = input("	-And fruity flavors? ")
		drink = {'strong': strong_pref, 'salty': salty_pref, 'bitter': bitter_pref, 'fruity': fruity_pref}
		repeat = False
		try:
			for flav in drink.keys():
				if drink.get(flav).upper() == "YES":
					drink[flav] = True
				elif drink.get(flav).upper() == "NO":
					drink[flav] = False
				else:
					print ("Sorry to ask again, but I got a bit confused.  Simple 'Yes' or 'No' will do.")
					repeat = True
		except:
			print ("Sorry to ask again, but I got a bit confused.  Simple 'Yes' or 'No' will do.")
			repeat = True
	print ("Ok I got all that!  I'll mix it up!")
	return drink

def drink_mix (drink):
	"""I mix up a random drink based on what the customer likes"""
	your_drink = []
	import random
	ingredients = {
    "strong": ["glug of rum", "slug of whisky", "splash of gin"],
    "salty": ["olive on a stick", "salt-dusted rim", "rasher of bacon"],
    "bitter": ["shake of bitters", "splash of tonic", "twist of lemon peel"],
    "fruity": ["slice of orange", "dash of cassis", "cherry on top"],
	}
	for d in drink.keys():
		new_ing = random.choice(ingredients[d])
		your_drink.append(new_ing)
		print (your_drink)
	print (your_drink)
		




