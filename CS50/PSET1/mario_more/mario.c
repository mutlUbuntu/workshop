#include <stdio.h>
#include <cs50.h>

int main(void)

{
    // This two variables for # symbol and space

    string has = "#";
    string spa = " ";
    
    //This variable is for user integer input named num.

    int num;

    // do..while loop for restiriction. If user enter a number in range, the code will work, 
    //otherwise program ask again for input.
    
    do
    
    {

//It work until user enter an integer intput betweet 1 and 8. This two numbers are include.

        num = get_int("Height: ");
        
    }
    
    //This is our condition.
    
    while (num < 1 || num > 8);
    
    //First for loop determines condition of user input. Program works *num times.
    
    for (int i = 0; i < num; i++)
    
    {
        //This loop works for required spaces.
        
        for (int j = 0; j < num - i - 1; j++)
        
        {
           
            printf("%s", spa);
            
        }
        
        //This loop works for required #s.
        
        for (int m = 0 ; m < i + 1 ; m++)
        
        {
        
            printf("%s", has);
        
        }
        
        //This printf is depend on first for loop for two space
        printf("%s%s", spa, spa);
        
        //This loop for # character after space
        for (int k = 0; k < i + 1; k++)
        
        {
            printf("%s", has);
        }
        
        //This printf works depend on the first for loop to pass next line. 
        printf("\n");
    }
    
    
}
