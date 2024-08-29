#include <stdio.h>
#include <stdlib.h>
#include <cs50.h>
#include <string.h>

int main(void)
{
    char *filename = malloc(3);
    sprintf(filename, "%03i.jpg", 2);

    FILE *output = fopen(filename, "w");
}