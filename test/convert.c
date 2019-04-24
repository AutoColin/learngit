#include <stdio.h>

int main(void)
{
    float num = 0;
    printf("Please enter the value to convert:");
    scanf("%f", &num);
    printf("Convert result:%-5.2f\n", num * 2.54);   
}
