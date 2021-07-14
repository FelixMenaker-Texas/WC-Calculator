import requests
from wc_requirement_dicts import c1,c2,c3,c4,c5,c6,c7,c8,c9,c10,c11,c12,c13,c14,c15,c16,c17,c18,c19,c20,c21,c22,c23,c24,c25,c26,c27,c28,c29,c30,c31,c32,c33,c34,c35,c36,c37,c38

def commas_cost(number):
    return ("{:,}".format(number))

#Get user-specific input
user_city = int(input("Your current city count: "))
user_api_key = input("Your API key (found at the bottom of https://politicsandwar.com/account/#4): ")
user_steel = int(input("Your current steel (integer): "))
user_alum = int(input("Your current aluminum (integer): "))
user_gas = int(input("Your current gasoline (integer): "))
user_muni = int(input("Your current munitions (integer): "))
user_uranium = int(input("Your current uranium (integer): "))
user_coal = int(input("Your current coal (integer): "))
user_food = int(input("Your current food (integer): "))
user_money = int(input("Your current money (integer): "))
user_MNI = float(input("Your current Monetary Net Income (found at the bottom of https://politicsandwar.com/nation/revenue/): "))

#Initialize the resources and prices lists
resources = ['steel', 'aluminum', 'gasoline', 'munitions', 'uranium', 'coal', 'food']
prices = []

#Gather the average prices from the API with the user's API key, JSON format things, then add average prices into the list prices
for x in resources:
    link = f"https://politicsandwar.com/api/tradeprice/?resource={x}&key={user_api_key}"
    raw = requests.get(link).json()
    prices.append(int(raw['avgprice']))

#Add 1 into the last slot of the prices list to account for cash
prices.append(1)

#Select the right dictionary for the user's number of cities (references wc_requirement_dicts.py file)
#I am literally too stupid to figure out how to import this automatically from the WC Google sheet, so the dictionaries would need to be
#manually updated if WC requirements change from what they were on 11 July 2021
if user_city == 1:
    c = c1
elif user_city == 2:
    c = c2
elif user_city == 3:
    c = c3
elif user_city == 4:
    c = c4
elif user_city == 5:
    c = c5
elif user_city == 6:
    c = c6
elif user_city == 7:
    c = c7
elif user_city == 8:
    c = c8
elif user_city == 9:
    c = c9
elif user_city == 10:
    c = c10
elif user_city == 11:
    c = c11
elif user_city == 12:
    c = c12
elif user_city == 13:
    c = c13
elif user_city == 14:
    c = c14
elif user_city == 15:
    c = c15
elif user_city == 16:
    c = c16
elif user_city == 17:
    c = c17
elif user_city == 18:
    c = c18
elif user_city == 19:
    c = c19
elif user_city == 20:
    c = c20
elif user_city == 21:
    c = c21
elif user_city == 22:
    c = c22
elif user_city == 23:
    c = c23
elif user_city == 24:
    c = c24
elif user_city == 25:
    c = c25
elif user_city == 26:
    c = c26
elif user_city == 27:
    c = c27
elif user_city == 28:
    c = c28
elif user_city == 29:
    c = c29
elif user_city == 30:
    c = c30
elif user_city == 31:
    c = c31
elif user_city == 32:
    c = c32
elif user_city == 33:
    c = c33
elif user_city == 34:
    c = c34
elif user_city == 35:
    c = c35
elif user_city == 36:
    c = c36
elif user_city == 37:
    c = c37
elif user_city == 38:
    c = c38
else:
    print("Not a valid city number")

#Calculate how much of each resource is needed by subtracting the user's input amount from the WC requirement in the corresponding city dictionary
needs_steel = c["steel"] - user_steel
needs_alum = c["alum"] - user_alum
needs_gas = c["gas"] - user_gas
needs_muni = c["muni"] - user_muni
needs_uranium = c["uranium"] - user_uranium
needs_coal = c["coal"] - user_coal
needs_food = c["food"] - user_food
needs_money = c["money"] - user_money

#Put the WC required amounts into a list for easier manipulation later
wc = [c["steel"],c["alum"],c["gas"],c["muni"],c["uranium"],c["coal"],c["food"],c["money"]]

#Make sure that any resources held over the required WC amount don't count
if needs_steel <= 0:
    needs_steel = 0
if needs_alum <= 0:
    needs_alum = 0
if needs_gas <= 0:
    needs_gas = 0
if needs_muni <= 0:
    needs_muni = 0
if needs_uranium <= 0:
    needs_uranium = 0
if needs_coal <= 0:
    needs_coal = 0
if needs_food <= 0:
    needs_food = 0
if needs_money <= 0:
    needs_money = 0

#Put the needed resource amounts into a list for easier manipulation later
needs = [needs_steel, needs_alum, needs_gas, needs_muni, needs_uranium, needs_coal, needs_food, needs_money]

#Return how much of each resource is needed to the user
print("You need " + str(commas_cost(needs_steel)) + " steel, " + str(commas_cost(needs_alum)) + " aluminum, " + str(commas_cost(needs_gas)) + " gasoline, "
      + str(commas_cost(needs_muni)) + " munitions, " + str(commas_cost(needs_uranium)) + " uranium, " + str(commas_cost(needs_food)) + " food, and " + "$"
      + str(commas_cost(needs_money)) + "\n")

#Return the cost of all needed resources, based on average prices, to the user
print("At current average prices: ")

needs_cost_list = [a * b for a,b in zip(prices,needs)]
needs_cost = sum(needs_cost_list)
print("It will cost $" + str(commas_cost(needs_cost)) + " to complete your warchest")

#Return the total WC cost to the user
total_wc_cost = [a * b for a,b in zip(prices,wc)]
tot_sum = sum(total_wc_cost)
print("The total warchest cost for " + str(user_city) + " cities is $" + str(commas_cost(tot_sum)))

#Return the % of the WC the user has currently based on monetary value (NOT based on number of resources, eg $1,000/$1,000 worth of uranium, not 5/5 uranium)
percent_done = (1-(needs_cost/tot_sum)) * 100
print("You are " + str(round(percent_done,2)) + "% of the way there.")

#Return the number of days the user needs to complete the WC at current average prices and their current Monetary Net Income
days = needs_cost / user_MNI
print("You will need " + str(round(days,2)) + " days to save up.")

#To prevent it from closing out immediately
input()