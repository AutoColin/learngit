#include <stdio.h>
#include <string.h>
#include <stdlib.h>

int main()
{
    unsigned char tmp[2];
    signed char src[3] = "AB";
    unsigned char des[2];
    unsigned int bytes;
    sprintf(tmp, "%c%c", src[0], src[1]);
    printf("%c %c\n", *src, *(src + 1));
    printf("%d %d\n", tmp[0], tmp[1]);
    printf("%c %c\n", tmp[0], tmp[1]);
    sscanf(tmp, "%x", &bytes);
    des[0] = bytes;
    printf("%x\n", bytes);
    printf("%x\n", des[0]);
    sscanf("gAB", "%x", &bytes);
    printf("%d\n", bytes);
}
