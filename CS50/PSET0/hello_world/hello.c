#include <stdio.h>
#include <cs50.h>

int main(void)
{
    // Thanks for CS50 :)
    printf("Hello, This is CS50.\n");
    //We need a user input to say hello!
    string name = get_string("What is your name\n");
    //After user writes a name, program says hello. 
    printf("Hello, %s\n", name);
    
}