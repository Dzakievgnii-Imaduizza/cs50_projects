#include <cs50.h>
#include <stdio.h>

int get_height(void);
void print_spaces(int);
void print_tags(int);
void print_distance(int);
int main(void)
{
    int height = get_height();
    int height2 = height;
    int distance = 2;
    int tags_ammount = 1;
    for(int i = 0; i < height;i++){
        print_spaces(height2);
        print_tags(tags_ammount);
        print_distance(distance);
        print_tags(tags_ammount);
        printf("\n");
        height2--;
        tags_ammount++;
    }
}

int get_height(void){
    int result;
    do{
        result = get_int("Height: ");
    }while(result < 1||result >8);

    return result;
}

void print_spaces(int height){
    int space = height - 1;
    for(int j = 0; j < space; j++){
        printf(" ");
    }
}

void print_tags(int height){
    int tags = height;
    for(int k = 0; k<tags; k++){
        printf("#");
    }
}

void print_distance(int length){
    for(int l = 0; l < length; l++){
        printf(" ");
    }
}