#include <stdio.h>
#include <string.h>
#include <stdio.h>
#include <map.h>

int solve1(int input, int sum) {
     
    if (input == 0) {
        return sum;
    }
    else {
        sum = sum * input;
        return solve1(input - 1, sum);
    }
}

int solve2(int input, int sum) {
    
}



class Number {
    int a;
};


int main()
{
    //judge
    //
    int factorial[]      = {0, 1, 2, 3, 4, 5};
    int factorial_real[] = {1.1, 2.2, 3.3, 4.4, 5.5};
    for (int index = 0; index < (int)sizeof(factorial)/sizeof(factorial[0]); index++) {
        printf("result = %d\n", solve1(factorial[index], 1));
    }
    printf("\n");


    for (int index = 0; index < (int)sizeof(factorial)/sizeof(factorial[0]) ; index++) {
        //printf("result  = %d\n", solve2(factorial[index]));
    }

    return 0;
}
