PYTHON DATA STRUCTURES AND LOOPS
Looping Coffee Chatbot
When in doubt, drink more coffee!

In the previous Coffee Chatbot project, you learned to build a Python chatbot for ordering one cup of coffee by leveraging recursive functions, user inputs, and print statements. The solution code from that project is carried over here. Now, it’s time to take this chatbot to the next level by adding loops!

Loops allow us to perform some action repeatedly – such as placing an order for multiple drinks – without needing to write an excess amount of code. You’ll be doing this here! Write all your code in the file called script.py and run it by entering python3 script.py in the terminal.

Let’s get started!

Tasks
13/13Complete
Mark the tasks as complete by checking them off
1.
Take a moment to review the code in script.py as well as the extra functions in utils.py. What do you think will happen as you make a selection for each step of your coffee order? Try running the script to see the chatbot in action!

As you progress through the project, feel free to run the script at any point to see your changes. Don’t forget to click the Save button first.

2.
Recall that we previously used recursive functions to repeat each selection process until the user enters an acceptable input. Now, let’s try using loops!

First, define a function called order_mocha() that prompts the user:

Would you like to try our limited-edition peppermint mocha?
[a] Sure!
[b] Maybe next time!
Use the input() function to get the user input and store the response in a variable called res.


Hint
Define order_mocha():

def order_mocha():
  res = input('Would you like to try our limited-edition peppermint mocha? \n[a] Sure! \n[b] Maybe next time! \n> ')
3.
Now, inside order_mocha(), move the input statement inside a while loop that has the condition True. This would create an infinite loop that continuously prompts the user for an input.

DO NOT run your program at this step — an infinite loop could crash your browser window!


Hint
Wrap the input statement inside a while loop:

def order_mocha():
  while True:
    res = input('Would you like to try our limited-edition peppermint mocha? \n[a] Sure! \n[b] Maybe next time! \n> ')
4.
Next, we want to terminate the loop once the user makes a recognizable selection – in this case, if the user enters either an 'a' or 'b'.

One way to break out of a loop – if the loop is located inside a function – is to simply return from that function.

Inside the while loop in order_mocha(), add conditional statements such that:

If res is equal to 'a', return the string 'peppermint mocha'
Else if res is equal to 'b', return the string 'mocha'

Hint
Add the conditional statements to order_mocha():

def order_mocha():
  while True:
    res = input('Would you like to try our limited-edition peppermint mocha? \n[a] Sure! \n[b] Maybe next time! \n> ')

    if res == 'a':
      return 'peppermint mocha'
    elif res == 'b':
      return 'mocha'
5.
If neither 'a' nor 'b' is chosen, the chatbot will ask the user the same question again and again until they select one of the two options. Let’s make this process a bit more user friendly!

Recall that in utils.py, we’ve written a function called print_message() that prints a message reminding the user to make a recognizable selection. At the end of the while loop in order_mocha(), call print_message() to print this reminder before it moves on to the next iteration of the loop.


Hint
Add call to print_message():

def order_mocha():
  while True:
    res = input('Would you like to try our limited-edition peppermint mocha? \n[a] Sure! \n[b] Maybe next time! \n> ')

    if res == 'a':
      return 'peppermint mocha'
    elif res == 'b':
      return 'mocha'

    print_message()
6.
Now, let’s call the order_mocha() function!

In get_drink_type(), instead of returning the string 'mocha' if the user selects mocha as their drink of choice, return the value that is returned from calling order_mocha().

Run your code and see what happens when you try ordering a mocha.


Hint
Update get_drink_type() to call order_mocha() if a mocha is ordered:

def get_drink_type():
  res = input('What type of drink would you like? \n[a] Brewed Coffee \n[b] Mocha \n[c] Latte \n> ')

  if res == 'a':
    return 'brewed coffee'
  elif res == 'b':
    return order_mocha()
  elif res == 'c':
    return order_latte()
  else:
    print_message()
    return get_drink_type()
7.
Next up, let’s add the functionality for ordering multiple drinks!

We’ll first need to create a variable to keep track of whether or not the user wants to order an additional drink. Inside coffee_bot(), below the initial welcome greeting, create a variable called order_drink and assign to it the string 'y' for yes as the default.

Now, move the next four lines of code inside a while loop that checks if order_drink equals to 'y', so that the chatbot will continuously take more orders if this condition is met.


Hint
Define order_drink and wrap the code for ordering a drink inside a while loop:

def coffee_bot():
  print('Welcome to the cafe!')

  order_drink = 'y'

  while order_drink == 'y':
    size = get_size()  
    drink_type = get_drink_type()

    drink = '{} {}'.format(size, drink_type)
    print('Alright, that\'s a {}!'.format(drink))
8.
In order to avoid an infinite loop, we need to add the option for changing order_drink to something other than 'y'.

At the end of the while loop, prompt the user:

Would you like to order another drink? (y/n)
Use the input() function to get the user input and store the response in order_drink.

This gives users the option to input 'n' for no more orders and break out of the loop.


Hint
Ask the user if they would like to order another drink:

def coffee_bot():
  print('Welcome to the cafe!')

  order_drink = 'y'

  while order_drink == 'y':
    size = get_size()  
    drink_type = get_drink_type()

    drink = '{} {}'.format(size, drink_type)
    print('Alright, that\'s a {}!'.format(drink))

    order_drink = input('Would you like to order another drink? (y/n) \n> ')
9.
You may have noticed that if the user inputted anything other than a 'y' or 'n', they would have also exited the loop! Instead, we’d want to continually prompt the user for a response until they input one of these two letters. This calls for another – you guessed it – while loop!

Move the input statement inside a while loop that has the condition True. Note that this new while loop should be nested inside the first while loop, right below the print statement that echoes back the drink name.


Hint
Wrap the input statement inside a while loop:

def coffee_bot():
  print('Welcome to the cafe!')

  order_drink = 'y'

  while order_drink == 'y':
    size = get_size()  
    drink_type = get_drink_type()

    drink = '{} {}'.format(size, drink_type)
    print('Alright, that\'s a {}!'.format(drink))

    while True:
      order_drink = input('Would you like to order another drink? (y/n) \n> ')
10.
Inside your new inner while loop, add an if statement that checks if order_drink is equal to 'y' or 'n'. Break out of the loop if it is equal to either.


Hint
Add an if statement for breaking out of the loop. Here’s one way to do this:

def coffee_bot():
  print('Welcome to the cafe!')

  order_drink = 'y'

  while order_drink == 'y':
    size = get_size()  
    drink_type = get_drink_type()

    drink = '{} {}'.format(size, drink_type)
    print('Alright, that\'s a {}!'.format(drink))

    while True:
      order_drink = input('Would you like to order another drink? (y/n) \n> ')

      if order_drink in ['y', 'n']:
        break
11.
Great job! Customers are now able to place multiple drink orders. As the final step, we’ll have the chatbot echo back all the drink names.

Inside coffee_bot(), right before your outer while loop, create an empty list called drinks that will store the names of all ordered drinks.

Then, inside the loop, right before asking the user if they’d like to place another order, append the currently ordered drink to the list drinks.


Hint
Append each ordered drink to the list drinks:

def coffee_bot():
  print('Welcome to the cafe!')

  order_drink = 'y'
  drinks = []

  while order_drink == 'y':
    size = get_size()  
    drink_type = get_drink_type()

    drink = '{} {}'.format(size, drink_type)
    print('Alright, that\'s a {}!'.format(drink))
    drinks.append(drink)

    while True:
      order_drink = input('Would you like to order another drink? (y/n) \n> ')

      if order_drink in ['y', 'n']:
        break
12.
Finally, outside of the while loop, create a for loop that will iterate over each order in drinks and print out the name:

Okay, so I have:
- ...
- ...
- ...
The chatbot is now complete! Run your code and order your favorite coffee drink. Order your friend’s favorite drink too!


Hint
Print out the list of drinks:

def coffee_bot():
  print('Welcome to the cafe!')

  order_drink = 'y'
  drinks = []

  while order_drink == 'y':
    size = get_size()  
    drink_type = get_drink_type()

    drink = '{} {}'.format(size, drink_type)
    print('Alright, that\'s a {}!'.format(drink))
    drinks.append(drink)

    while True:
      order_drink = input('Would you like to order another drink? (y/n) \n> ')

      if order_drink in ['y', 'n']:
        break

  print('Okay, so I have:')

  for drink in drinks:
    print('-', drink)
Bonus Task
13.
Try finding more ways you can use loops to extend this chatbot! For example:

Add an additional type of drink or an additional option to an existing drink
Allow the chatbot to recognize additional inputs besides 'y' and 'n' – such as 'yes', 'sure', or 'nah' – when it asks the user if they would like another drink
Allow the chatbot to recognize key exit words such as 'stop' or 'bye' that can terminate the order at any step
Feel free to get creative!