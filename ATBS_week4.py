'''--------By: PJ Sheldon---------
	--------Date: 7/29/20---------
	ATBS_week4.py Sandwhich maker
	SEC-290 Wilmington University'''

import pyinputplus as pyip

# prices for all the variables of sandwhich parts
wheatprice = 1.99
whiteprice = 1.99
sourdoughprice = 2.99
chickenprice = 3.99
turkeyprice = 3.50
hamprice = 2.20
tofuprice = 4.50
cheddarprice = 0.99 
swissprice = 1.00
mozzarellaprice = 0.50
nocheeseprice = 0.00
condomentprice = 1.99
nocondomentprice = 0.00

def reciept():
	print('Great! Here is your recipt: ')                    # start of reciepts and total
	print(" ")
	if bread == 'Wheat':
		breadprice = wheatprice                               # if bread
		print('{} | ${:.2f}'.format(bread, wheatprice))
	elif bread == 'White':
		breadprice = whiteprice
		print('{} | ${:.2f}'.format(bread, whiteprice))
	elif bread == 'Sourdough':
		breadprice = sourdoughprice
		print('{} | ${:.2f}'.format(bread, sourdoughprice))
	if protein == 'Chicken':                                   # if protein
		proteinprice = chickenprice
		print('{} | ${:.2f}'.format(protein, chickenprice))
	elif protein == 'Turkey':
		proteinprice = turkeyprice
		print('{} | ${:.2f}'.format(protein, turkeyprice))
	elif protein == 'Ham':
		proteinprice = hamprice
		print('{} | ${:.2f}'.format(protein, hamprice))
	elif protein == 'Tofu':
		proteinprice = tofuprice
		print('{} | ${:.2f}'.format(protein, tofuprice))
	if cheese == 'Cheddar':                                     # If cheese
		cheprice = cheddarprice
		print('{} | ${:.2f}'.format(cheese, cheddarprice))
	elif cheese == 'Swiss':
		cheprice = swissprice
		print('{} | ${:.2f}'.format(cheese, swissprice))
	elif cheese == 'Mozzarella':
		cheprice = mozzarellaprice
		print('{} | ${:.2f}'.format(cheese, mozzarellaprice))
	elif cheese == 'no cheese':
		cheprice = nocheeseprice
	if 	condo == 'Mayo, Mustard, Lettuce, and Tomato':         # if condoment
		condoprice = condomentprice
		print('Condoments | ${:.2f}'.format(condomentprice))
	elif condo == 'no Mayo, Mustard, Lettuce, and Tomato':
		condoprice = nocondomentprice
	print(" ")
	print('For {} sandwhich(es)'.format(howMany))              # how many sandwiches        
	print(" ")
	total = breadprice + proteinprice + cheprice + condoprice * howMany   # the grand total 
	print('Total is: ${:.2f}'.format(total))	                         # printed grand total






print("THIS IS THE SANDWHICH MAKER") # Title of the program 
print(" ") # spacing 
print('Instructions: Please select the number or the name of your choice when prompted. \nAfter you have selected all the choices then we will let you know the price.')
print(" ")

# Select a type of bread 
print("Choose what type of bread:") # Question for bread
bread = pyip.inputMenu(['Wheat', 'White', 'Sourdough'], numbered=True) # variable of choices using the pyinputplus inputMenu with the ability to have numbered choices

print('You chose ' + bread + ' bread.')
print(" ")

# Select a protein  
print("Choose what type of protein:")
protein = pyip.inputMenu(['Chicken', 'Turkey', 'Ham', 'Tofu'], numbered=True) # protien choices

print('You chose ' + protein) # result
print(" ")

# Cheese question

print("Do you want cheese? yes or no") # yes no question
cheeseQuest = pyip.inputYesNo() 
print('You chose ' + cheeseQuest) # result

if cheeseQuest == 'yes':
	print('what kind of cheese do you want?')
	cheese = pyip.inputMenu(['Cheddar', 'Swiss', 'Mozzarella'], numbered=True) # cheese choices
	print('You chose ' + cheese) # result
	print(" ")
elif cheeseQuest == 'no': # no result 
	cheese = "no cheese" # no cheese variable 
	print(" ")

# Condoment question

print("Do you want Mayo, Mustard, Lettuce, or Tomato? yes or no") # question
condoQuest = pyip.inputYesNo() # input
print('you chose ' + condoQuest) # result

if condoQuest == 'yes': # if yes
	condo = "Mayo, Mustard, Lettuce, and Tomato" 
	print('Adding ' + condo) # result
	print(" ")
elif condoQuest == 'no': # if no 
	condo = "no Mayo, Mustard, Lettuce, and Tomato" # result to be later in the program 
	print(" ")

# How many sandwhiches

howMany = pyip.inputInt("How many sandwhiches do you want? ", min=1) # has to have at least one sandwhich
print(howMany) # result 
print(" ")

# Result

print('You want {} Sandwhich(es) with {} and {} on {} with {}.'.format(howMany, protein, cheese, bread, condo)) # repeat the order bask
print('is this correct? Yes or no?') # make sure the order was correct
answer = pyip.inputYesNo()
print(" ")
if 'yes' in answer: # if yes
	reciept() # self defined function 
elif 'no' in answer:  # in no 
	print('Sorry about that, please restart Sandwhich Maker!') # result of if no