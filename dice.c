#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int roll(int dicenum, int numroll){
    int value = 0;
    srand(time(NULL));
    for (int i = 0; i < numroll; i++){
        value += (rand() % dicenum) + 1;
    }
    return value;
}