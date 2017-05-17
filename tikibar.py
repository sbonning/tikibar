##Sam's Tiki Bar project in the "Pirate Bartender" Assignment for Thinkful
##Mixing delicious tiki drinks since 2017!
##Description of functionality:
## - the Bartender will ask a series of questions about your tastes
## - the Bartender will mix you up a delicious beverage/s until you are done!

def drink_program ():
	"""Ties the entire program together"""
	print ("Here you go!")

def glass_pref ():
	"""I welcome the customer and choose a glass for the drink"""
	print ("A bartender with one eye greets you with a smile.  Or a grimace.  It's hard to tell.\n")
	print ("	Welcome to Sam's Tiki Bar!")
	print ("	First choose your glassware.  We pride ourselves on our original Tiki mugs!")
	print ("	What are you thinking: Novelty animal, or one of our Culural options?\n")
	print ("The bartender shows you a selection of mugs, including a Lucky Cat, a terrifying looking Fu Man Chu, and a Bikini-clad dancer")
	glass = input("If you want one of those cute animals, choose 1. For the cultural option, choose 2:  ")
	# how do I add a space between the two options?
	print ("Great choice. I love a good {}.".format(glass))

def drink_prefs (strong,salty,sweet,fruity):
	"""I choose a glass, and I gather the input about customer taste preferences"""
	print ("Welcome to Sam's Tiki Bar!")
