#include <cs50.h>
#include <stdio.h>

int get_startsize(void);
int get_endsize(int start);
int main(void)
{
    // TODO: Prompt for start size
    int start_size = get_startsize();
    // TODO: Prompt for end size
    int end_size = get_endsize(start_size);
    // TODO: Calculate number of years until we reach threshold
    int years = 0;
    while(start_size < end_size){
        start_size = start_size + (start_size/3) - (start_size/4);
        years ++;
    }

    // TODO: Print number of years
    printf("Years: %i\n", years);
}

int get_startsize(void)
{
    int n;
    do{
        n = get_int("Start size: ");

    }while(n < 9);
    return n;
}

int get_endsize(int start)
{
    int end;
    do{
        end = get_int("End size: ");

    }while (end < start);
    return end;
}