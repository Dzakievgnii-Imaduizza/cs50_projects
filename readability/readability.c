#include <cs50.h>
#include <stdio.h>
#include <string.h>
#include <math.h>

int count_grade(string text);
int count_letters(string txt);
int count_words(string txt);
int count_sentences(string txt);

int main(void)
{
    string text = get_string("Text: ");
    int grade = count_grade(text);

    if (grade < 1)
    {
        printf("Before Grade 1\n");
    }
    else if (grade > 16)
    {
        printf("Grade 16+\n");
    }
    else
    {
        printf("Grade %i\n", grade);
    }

}

int count_grade(string text)
{
    int letters = count_letters(text);
    int words = count_words(text);
    int sentences = count_sentences(text);
    int result;
    float index;
    float x = 100 / (float)words;
    float l = letters * x;
    float s = sentences * x;
    index = 0.0588 * l - 0.296 * s - 15.8;
    result = (int)round(index);
    return result;


}

int count_letters(string txt)
{
    int total_letters = 0;
    for (int i = 0; i < strlen(txt); i++)
    {
        if (txt[i] > 64 && txt[i] < 91)
        {
            total_letters++;
        }
        else if (txt[i] > 96 && txt[i] < 123)
        {
            total_letters++;
        }
    }
    return total_letters;
}

int count_words(string txt)
{
    int total_words = 0;
    for (int i = 0; i < strlen(txt); i++)
    {
        if (txt[i] == 32)
        {
            total_words++;
        }
    }
    return total_words + 1;
}

int count_sentences(string txt)
{
    int total_sentences = 0;
    for (int i = 0; i < strlen(txt); i++)
    {
        if (txt[i] == 46 || txt[i] == 33 || txt[i] == 63)
        {
            total_sentences++;
        }
    }
    return total_sentences;
}