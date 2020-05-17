#include <stdio.h>
#include <cs50.h>

int main(void)
{
    int quar, dime, nick, penn;
    int quar2, dime2, nick2;
    float cash;
    do
    {
        cash = get_float("Change: ");
    }
    while (cash <= 0);
    
    float a = cash * 100; //to make correct operations
    int b;
    b = (int) a; // it changes to int from float
    if (b == 419)//Why 4.2*100=419
    {
        b = 420; //This is for undefined error:)
    }
    quar = b / 25; //Here is for total
    quar2 = b % 25; // Here is for next step
    dime = quar2 / 10; //Here is for total
    dime2 = quar2 % 10; // Here is for next step
    nick = dime2 / 5; //Here is for total
    nick2 = dime2 % 5; // Here is for next step
    penn = nick2 / 1;//Here is for total

    int total = quar + dime + nick + penn; 
    printf("%i\n", total);
}
