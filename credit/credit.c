#include <cs50.h>
#include <stdio.h>

string calculate_16(long number);
string calculate_15(long number);
string calculate_13(long number);
int main(void)
{
    string validity = "";
    long card_number;
    //prompt user
    do{
        card_number = get_long("Number: ");
    }while(card_number < 1);
    //if the card is 16 digits
    if(card_number / 1000000000000000 > 0 && card_number / 1000000000000000 < 10)
    {
        validity = calculate_16(card_number);
        printf("%s\n", validity);
    }
    // if card is 15 digits
    else if(card_number / 100000000000000 > 0 && card_number / 100000000000000 < 10)
    {
        validity = calculate_15(card_number);
        printf("%s\n", validity);
    }
    // if card is 13 digits
    else if(card_number / 1000000000000 > 0 && card_number / 1000000000000 < 10)
    {
       validity = calculate_13(card_number);
        printf("%s\n", validity);
    }
    //if card is not 13,15, or 16 digits
    else
    {
        validity = "INVALID";
        printf("%s\n", validity);
    }

}

string calculate_16(long number)
{
    string result = "";
    long modulo = 10;
    long devider = 1000000000000000;
    long total = 0;
    long digits = 0;
    long devider2 = 100000000000000;
    while (devider >= 10)
    {
        if(((number/devider) % modulo) * 2 < 10)
        {
            digits = ((number/devider) % modulo) * 2;
        }
        else if(((number/devider) % modulo) * 2 >= 10)
        {
            digits = (((number/devider) % modulo) * 2) / 10 + (((number/devider) % modulo) * 2) % 10;
        }
        devider = devider/100;
        total = total + digits;
    }
    while (devider2 >= 1)
    {
        digits = ((number/devider2) % modulo);

        devider2 = devider2/100;
        total = total + digits;
    }
    if(total % 10 == 0)
    {
        if(number/1000000000000000 == 4)
        {
            result = "VISA";
        }
        else if(number/100000000000000 == 51||number/100000000000000 == 52||number/100000000000000 == 53||number/100000000000000 == 54||number/100000000000000 == 55)
        {
            result = "MASTERCARD";
        }
        else
        {
            result = "INVALID";
        }
    }
    else
    {
        result = "INVALID";
    }
    return result;
}



string calculate_15(long number)
{
    string result = "";
    long modulo = 10;
    long devider = 10000000000000;
    long total = 0;
    long digits = 0;
    long devider2 = 100000000000000;
    while (devider >= 10)
    {
        if(((number/devider) % modulo) * 2 < 10)
        {
            digits = ((number/devider) % modulo) * 2;
        }
        else if(((number/devider) % modulo) * 2 >= 10)
        {
            digits = (((number/devider) % modulo) * 2) / 10 + (((number/devider) % modulo) * 2) % 10;
        }
        devider = devider/100;
        total = total + digits;
    }
    while (devider2 >= 1)
    {
        digits = ((number/devider2) % modulo);

        devider2 = devider2/100;
        total = total + digits;
    }
    if(total % 10 == 0)
    {
        if(number/10000000000000 == 34||number/10000000000000 == 37)
        {
            result = "AMEX";
        }else
        {
            result = "INVALID";
        }
    }else
    {
        result = "INVALID";
    }
    return result;
}

string calculate_13(long number)
{
    string result = "";
    long modulo = 10;
    long devider = 100000000000;
    long total = 0;
    long digits = 0;
    long devider2 = 1000000000000;
    while (devider >= 10)
    {
        if(((number/devider) % modulo) * 2 < 10)
        {
            digits = ((number/devider) % modulo) * 2;
        }
        else if(((number/devider) % modulo) * 2 >= 10)
        {
            digits = (((number/devider) % modulo) * 2) / 10 + (((number/devider) % modulo) * 2) % 10;
        }
        devider = devider/100;
        total = total + digits;
    }
    while (devider2 >= 1)
    {
        digits = ((number/devider2) % modulo);

        devider2 = devider2/100;
        total = total + digits;
    }
    if(total % 10 == 0){
        if(number/1000000000000 == 4)
        {
            result = "VISA";
        }else
        {
            result = "INVALID";
        }
    }else
    {
        result = "INVALID";
    }
    return result;
}