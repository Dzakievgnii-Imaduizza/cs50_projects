#include <cs50.h>
#include <stdio.h>
#include <string.h>

string substitute(string key, string text);
string makeupper(string orgtext);
bool check_number(string txt);
bool check_duplicate(string txt);

int main(int argc, string argv[])
{
    if (argc != 2)
    {
        printf("Usage: ./substitution key\n");
        return 1;
    }
    else if (strlen(argv[1]) != 26)
    {
        printf("Key must contain 26 characters.\n");
        return 1;
    }
    else if (check_number(argv[1]))
    {
        printf("Key must contain alphabetic letters.\n");
        return 1;
    }
    else if (check_duplicate(makeupper(argv[1])))
    {
        printf("Key must not contain repeated characters.\n");
        return 1;
    }
    else
    {
        string up_key = makeupper(argv[1]);
        string plaintxt = get_string("plaintext: ");
        string cyphertxt = substitute(up_key, plaintxt);
        printf("ciphertext: %s\n", cyphertxt);

    }

}

string substitute(string key, string text)
{
    string result = text;
    for (int i = 0; i < strlen(result); i++)
    {
        if (result[i] > 64 && result[i] < 91)
        {
            result[i] = key[result[i] - 65];
        }
        else if (result[i] > 96 && result[i] < 123)
        {
            result[i] = (char)key[result[i] - 97] + 32;
        }
    }
    return result;
}

string makeupper(string orgtext)
{
    string result = orgtext;
    for (int i = 0; i < strlen(result); i++)
    {
        if (result[i] > 96 && result[i] < 123)
        {
            result[i] = (char)result[i] - 32;
        }
    }
    return result;
}

bool check_number(string txt)
{
    bool result = true;
    for (int i = 0; i < strlen(txt); i++)
    {
        if (txt[i] > 64 && txt[i] < 91)
        {
            result = false;
        }
        else if (txt[i] > 96 && txt[i] < 123)
        {
            result = false;
        }
        else
        {
            result = true;
        }
    }
    return result;
}

bool check_duplicate(string txt)
{
    bool result = false;
    for (int i = 0 ; i < strlen(txt); i++)
    {
        for (int j = i + 1; j < strlen(txt); j++)
        {
            if (txt[i] == txt[j])
            {
                result = true;
            }
        }
    }
    return result;
}