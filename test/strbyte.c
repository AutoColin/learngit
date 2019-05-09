#include <stdio.h>
#include <string.h>
#include <stdlib.h>

void ByteToStr(char* src, int8_t* dest, int32_t len)
{
    int32_t i = 0;

    for(i = 0; i < len; i++)
    {
        sprintf(dest + i * 2, "%0.2x", src[i]);
    }

    return;
}

int32_t StrToByte(int8_t* src, char* dest)
{
    int32_t i = strlen(src), j = 0, count = 0;

    int8_t tmp[2];
    unsigned int bytes;

    for(j = 0; j < i; j++)
    {
        if(0 == j % 2)
        {
            sprintf(tmp, "%c%c", src[j], src[j + 1]);
            sscanf(tmp, "%x", &bytes);
            dest[count] = bytes;
            count++;
        }
    }

    return count;
}

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
