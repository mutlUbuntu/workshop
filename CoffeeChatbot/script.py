# -*- coding: utf-8 -*-

# Define your functions

def print_message():
  print("I'm sorry, I did not understand your selection. Please enter the corresponding letter for your response.")


def order_latte():
  res = input("And what kind of milk for your latte? \n[a] 2% milk \n[b] Non-fat milk \n[c] Soy milk\n")
  order = " "
  if res == "a":
    order = "Latte"
  elif res == "b":
    order = "non-fat latte"
  elif res == "c":
    order = "soy latte"
  else:
    print_message()
    return order_latte()
  return order


def get_drink_type():
  res = input("What type of drink would you like? \n[a] Brewed Coffee \n[b] Mocha \n[c] Latte\n")
  type_ = " "
  if res == "a":
    type_ = "Brewed Coffee"
  elif res == "b":
    type_ = "Mocha"
  elif res == "c":
    return order_latte()
  else:
    print_message()
    return get_drink_type()
  return type_


def get_size():
  res = input('What size drink can I get for you? \n[a] Small \n[b] Medium \n[c] Large \n> ')
  size = " "
  if res == "a":
    size = "Small"
  elif res == "b":
    size = "Medium"
  elif res == "c":
    size = "Large"
  else:
    print_message()
    return get_size()
  return size


def bye():
  name = input("Can I get your name please?\n")
  print("Thanks, " + name + "! Your drink will be ready shortly.")


def coffee_bot():
  print("Welcome to the cafe!")
  size = get_size()
  #print(size)
  drink_type = get_drink_type()
  #print(drink_type)
  print("Allright, that's a "+ size + " " + drink_type + "!")
  return bye()
  

coffee_bot()


