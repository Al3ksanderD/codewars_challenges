from collections import Counter

def string_to_dictionary(string):
    list = []
    list = string.split(";")
    count = Counter(list)
    return count

print(string_to_dictionary("Lama;Cos;alpaka;alpaka"))

"""
String to Dictionary
Implement a function string_to_dictionary which receives one parameter: string. This parameter contains a sequence of items (like sword, axe, etc) that are separated by semicolons (;). The function should return a dictionary, which contains the information on all items in the string, with their amounts. Example:

For string sword;axe;torch;axe;sword the expected return value is:

{
  "sword": 2,
  "axe": 2,
  "torch": 1
}"""



"""
Restaurant Bill A
This challenge consists of three functions:

read_restaurant_bill - read the data from given text file 
(example file is restaurant_bill.txt).
 Each line is a separate entry in a bill from a large restaurant dinner. 
 It consits of the meal's name, its quantity (how many times was it ordered) and its price (per meal).
  The data should be returned in a format of list of dictionaries, where a single dictionary represents a single entry. 
  Use the constants provided in the start code as dictionary keys. Example:
Input string:

Pizza - 2 - 25.00
Spaghetti - 1 - 15.00
Expected output:

[
  {"meal": "Pizza", "quantity": 2, "price": 25.00},
  {"meal": "Spaghetti", "quantity": 1, "price": 15.00}
]
get_meals_more_expensive_than - receives a parameter data_set,
 which is of the exact same format as the return value of read_restaurant_bill - 
 a list of dictionaries, representing a set of restaurant bill entries. 
 This function's purpose is to return a list of meals (just their names), 
 which are more expensive than the price parameter.
get_least_bought_meal - similarily to the above function, 
it receives a data_set. This function is supposed to return the name of the meal, 
which was ordered the least amount of times (its quantity is the lowest).

MEAL_KEY = "meal"
QUANTITY_KEY = "quantity"
PRICE_KEY = "price"
FILENAME = "restaurant_bill.txt"

def read_restaurant_bill(filename):
    pass

def get_meals_more_expensive_than(data_set, price):
    pass

def get_least_bought_meal(data_set):
    pass
    
Fried Chicken - 5 - 20.00
Spaghetti Bolognese - 2 - 15.50
Spaghetti Carbonara - 1 - 10.00
Pizza Pepperoni XL - 3 - 40.25
Spaghetti Napoli - 2 - 15.00
Schnitzel - 5 - 20.10
"""