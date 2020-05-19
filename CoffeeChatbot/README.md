Coffee Chatbot
But first, coffee.

Whether it’s to get us ready to jump-start our day or to get us through a late-night cram session, many of us need our regular caffeine fix! Ordering coffee is just one example of a process that can be automated with the help of a chatbot.

You’re given the task of creating a Python chatbot that can help cut the wait time of a normal coffee run by taking customers’ orders in advance. Write your code in the file called script.py and run it by entering python3 script.py in the terminal.

Let’s get started!

Tasks


1.
Define a function called coffee_bot() that prints out the statement:

Welcome to the cafe!
At the bottom of the script, call your function. Run the script to see the greeting!

As you progress through the project, feel free to run the script at any point to see your changes. Don’t forget to click the Save button first.


2.
Next, define a function called get_size() that will ask the user for the size of their drink. Use the input() function to get the user input and store the response in a variable called res:

res = input('What size drink can I get for you? \n[a] Small \n[b] Medium \n[c] Large \n> ')
Return res from the function. It should contain the letter corresponding to the selection.

Inside your coffee_bot() definition, call the get_size() function and store the returned value in a variable called size. Print out size to see the value!


3.
Now, update the get_size() function so that it returns the selected size instead of the letter corresponding to the user’s selection.

Specifically, delete your previous return statement and add conditional statements such that:

If res is equal to 'a', return the string 'small'
Else if res is equal to 'b', return the string 'medium'
Else if res is equal to 'c', return the string 'large'
Try running your script now and see what gets printed out.


4.
You may have noticed that if the user entered an input other than 'a', 'b', or 'c', None gets printed out. This is because we have not accounted for these kinds of responses in the conditional statements, and by default, a function will return None.

Let’s fix this! Add an else block to your conditional statements. Inside this block, call the get_size() function and return its returned value. This will continue prompting the user for a size selection until the user’s response matches one of our expected inputs.

Notice that the get_size() function is now calling itself, making it a recursive function. See this exercise on recursion to learn more about recursive functions.

Save your code and run the script by entering python3 script.py in the terminal to see it in action!


5.
The get_size() function is looking great! Lastly, just to make it slightly more user friendly, let’s have it print out a message in the else block before it prompts the user for an input again.

First, define a separate function called print_message() that prints the message:

I'm sorry, I did not understand your selection. Please enter the corresponding letter for your response.
Then, inside the else block of your get_size() function, call the print_message() function right before the return statement.


6.
Next up, define a function called get_drink_type() that will ask the user for their drink order:

What type of drink would you like?
[a] Brewed Coffee
[b] Mocha
[c] Latte
Use the input() function to get the user input and store the response in a variable called res. Return res for now.

Inside your coffee_bot() definition, under your call to get_size(), call the get_drink_type() function and store the returned value in a variable called drink_type. Print out drink_type to see the value!


7.
Similar to get_size(), delete your previous return statement in get_drink_type() and add conditional statements such that:

If res is equal to 'a', return the string 'brewed coffee'
Else if res is equal to 'b', return the string 'mocha'
Else if res is equal to 'c', return the string 'latte'
Otherwise, call print_message() and return the value that is returned from calling get_drink_type()


8.
Now, let’s take it a step further! If the user orders a latte, we’ll ask them what kind of milk they would like.

Define a function called order_latte() that prompts the user:

And what kind of milk for your latte?
[a] 2% milk
[b] Non-fat milk
[c] Soy milk
Use the input() function to get the user input and store the response in a variable called res.


9.
Add conditional statements to your order_latte() function such that:

If res is equal to 'a', return the string 'latte'
Else if res is equal to 'b', return the string 'non-fat latte'
Else if res is equal to 'c', return the string 'soy latte'
Otherwise, call print_message() and return the value that is returned from calling order_latte()


10.
In get_drink_type(), instead of returning the string 'latte' if the user selects latte as their drink of choice, return the value that is returned from calling order_latte().

Try running your script and see what gets printed out when you select latte as your drink!


11.
Now, let’s put it all together! In coffee_bot(), remove any print statements you currently have besides the welcome greeting.

Then, add a print statement at the very end that outputs:

Alright, that's a {size} {drink_type}!


12.
Next, prompt the user for their name:

Can I get your name please?
Use the input() function to get the user input and store the response in a variable called name.


13.
Finally, print out a statement that says:

Thanks, {name}! Your drink will be ready shortly.
Order complete!


Bonus Task
14.
Try adding some additional functionality to the chatbot. For example, how can we ask the user if they would like a plastic cup or to use their own reusable cup? How about if they’d like their drink hot or iced? Or maybe if they’d want to order an additional drink?

Feel free to get creative!