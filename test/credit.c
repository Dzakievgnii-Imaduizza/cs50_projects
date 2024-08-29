#include <stdio.h>
#include <cs50.h>

int main(void){
    long devider = 1000000000000;
    long result;
    while(devider >= 10){
        result = 4000000000080/devider % 10;
        printf("%li\n", result);
        devider = devider/100;
    }
}