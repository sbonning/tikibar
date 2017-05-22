##Sam's Tiki Bar project in the "Pirate Bartender" Assignment for Thinkful
##Mixing delicious tiki drinks since 2017!
##Description of functionality:
## - the Bartender will ask a series of questions about your tastes (mug and drink)
## - the Bartender will mix you up a delicious beverage/s until you are done!

def welcome ():
	"""Welcome the customer to the bar"""
	print ("\n\n\n\nA bartender with one eye greets you with a smile.  Or a grimace.  It's hard to tell.\n")
	print ("	-Welcome to Sam's Tiki Bar!")

def customer (customers):
	"""Asks for the customer name, and if they are a repeat customer will give them the same drink as before"""
	name = input("	-And what's your name, friend?")
	try:
		customers[name]
		if customers[name][1] == 'water':
			print ("Bartender scowls and pours you a water")
		else:
			print ("	-Oh {0}, I know you like a {3}, in a {1}, with {2}. Let me mix it up for you.".format(name, customers[name][0],customers[name][1],customers[name][2]))
		## Is there a better way to call a list in a dictionary entry other than x[y][z]?  This is not attractive
		new_customer = False
	except:
		print ("	-Oh, a newbie.  We'll fix something special up for you!")
		new_customer = True
	return name, new_customer
	# I'm only doing a tuple here because I can't work out how to change the value of new_customer otherwise

def glass_pref():
	"""Choose a glass for the drink"""
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
	print ("	-Great choice. I love a {}.".format(glassware.get(glass)))
	pauser = input("Hit any key to continue\n")
	return glassware.get(glass)

def drink_pref():
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
					## I would prefer for this line not to repeat - any suggestions
					repeat = True
		except:
			print ("Sorry to ask again, but I got a bit confused.  Simple 'Yes' or 'No' will do.")
			repeat = True
	print ("\n	-Ok I got all that!  I'll mix it up!")
	pauser = input("Hit any key to continue\n")
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
		if drink[d] == 1:
			your_drink.append(new_ing)
		else:
			continue
	if your_drink == []:
		print ("Well, it seems that you did something to offend the bartender, because he gave you a water.")
		ing_string = "water"
	else:
		ing_string = ""
		if len(your_drink) == 1:
			ing_string = your_drink[0]
		else:
			for a in your_drink[0:len(your_drink)-1]:
				ing_string = ing_string+a+", "
			ing_string = ing_string+"and "+ your_drink[len(your_drink)-1]+"."
	return ing_string
	## if i'd thought about the last problem with decreasing stock at the start, I wouldn't have created a string for the ing_string variable
	## but since I did I decided it was too much work to reverse it and do the stocktake

def deliver_drink(ing_string, glass, name, customers):
	"""Creates the drink for the new customer"""
	import random
	drink_name_set = {
	"first": ["Thirsty","Dancing","Cool","Flirty"],
	"second": ["Pelican", "Barbarian", "Hawaiian Girl", "Mule"]
	}
	drink_name = random.choice(drink_name_set["first"]) + " " + random.choice(drink_name_set["second"])
	if ing_string == "water":
		customers[name] = [glass, ing_string, drink_name]
		return customers
	else:
		print ("	-Here you go, {}.  I've mixed up a special one for you!".format(name))
		print ("	-In your {0}, highlights of {1}.  It's called {2}.".format(glass,ing_string, drink_name))
		customers[name] = [glass, ing_string, drink_name]
		print ("	-Enjoy! Let me know if you'd like another.\n")
		# new_customer = False
		# I tried to change new_customer to false here but it's not working.. so I had to to it in the drink_program function
		return customers


## I had to split out the "deliver_drink" from the "another_drink" function because I couldn't work out how to return multiple variables
## from deliver_drink and I had to save the updated customers dictionary so I couldn't update the another value for the variable 
## I think I have to return the updated value of another as a global variable to ensure that it updates in drink_program function?

def another_drink(another):
	"""Checks if you want another drink when you are done, new or existing customer"""
	another = input("Done already? Say yes if you'd like another.")
	if another.upper() == "YES":
		another = True
	else:
		another = False
	return another


def drink_program ():
	"""Ties the entire program together"""
	customers = {}
	another = True
	new_customer = True
	
	welcome()
	while another == True:
		name_new = customer(customers)
		name = name_new [0]
		if name_new[1] == False:
			new_customer = False
		else:
			new_customer = True
		## This seems also like not best practice - i'm parsing the tuple here because I couldn't work out how to set new_customer within the function

		while new_customer == True:
			glass = glass_pref()
			drink = drink_pref()
			ing_string = drink_mix(drink)
			customers = deliver_drink(ing_string, glass, name, customers)
			new_customer = False
		
		another = another_drink(another)
			## can we please talk about local v global variables here?  I'm not sure if I've done something strange with variable "another"
			## also i'm pretty sure I shouldn't be doing x = something(x), seems bad
	print("    -Thanks for drinking with us!")

if __name__ == "__main__":
	drink_program()

