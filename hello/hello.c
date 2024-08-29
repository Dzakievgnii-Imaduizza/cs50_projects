#include <cs50.h>
#include <stdio.h>

int main(void)
{
    //get user input
    string name = get_string("What's you're name: ");
    //say hello to user
    printf("Hello, %s\n", name);
}