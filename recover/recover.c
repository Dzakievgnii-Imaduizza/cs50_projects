#include <stdio.h>
#include <stdlib.h>

int main(int argc, char *argv[])
{
    if (argc != 2)
    {
        printf("Usage: ./recover IMAGE\n");
        return 1;
    }
    //Open File
    FILE *inputFile = fopen(argv[1], "r");
    if (inputFile == NULL)
    {
        printf("Could not open file\n");
        return 1;
    }
    unsigned char buffer[512];
    int counter = 0;
    char *fileName = malloc(3);
    FILE *outputFile = NULL;
    while (fread(buffer, 512, 1, inputFile) == 1)
    {
        if (buffer[0] == 0xff && buffer[1] == 0xd8 && buffer[2] == 0xff && (buffer[3] % 0xf0) == 0xe0)
        {
            if (counter == 0)
            {
                sprintf(fileName, "%03i.jpg", counter);
                outputFile = fopen(fileName, "w");
                fwrite(buffer, 512, 1, outputFile);
                counter++;
            }
            else
            {
                fclose(outputFile);
                sprintf(fileName, "%03i.jpg", counter);
                outputFile = fopen(fileName, "w");
                fwrite(buffer, 512, 1, outputFile);
                counter++;
            }
        }
        else
        {
            if (counter > 0)
            {
                fwrite(buffer, 512, 1, outputFile);
            }
        }
    }
    free(fileName);
    fclose(inputFile);
    fclose(outputFile);
    // here u go some comments
}