#include <stdio.h>
#include <stdlib.h>

int main(void)
{
    printf("begin cycle:\n");
    int8_t signal;
    while(1)
    {  
        //printf("input signal:");
        scanf("%d", &signal);
        printf("signal:%d\n", signal);
        if(signal > 0)
            continue;
        else 
            break;
    }
    printf("over\n");

    return 0;
}
