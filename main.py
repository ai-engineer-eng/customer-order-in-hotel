import time

#list of items in menu
menu = ["Burger", "Fries", "Soda", "Sushi", "Pizza"]
#waiter asking for order
waiter = input("Welcome to the restaurant! What would you like to order?").lower()
#customer asking for menue
if waiter == "menu please":
  print("Here it is: \n" + str(menu))
#asking after 5 seconds again for order after showing menu
  time.sleep(5)
#asking again for order after menu
  customer_order = input("What would you like to order?")
  if customer_order in menu:
    print("Okay, your order will be ready soon!")
  else:
    print("Sorry, we don't have that on the menu.")
else:
  print("You didn't ask for the menu." + "\n" + "Please ask for the menu.")
