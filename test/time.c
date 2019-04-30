#include <time.h>
#include <stdio.h>
#include <string.h>

int main(void)
{
    time_t timer;
    struct tm *tblock;
    timer = time(NULL);
    tblock = localtime(&timer);
    printf("Local time is: %s\n", asctime(tblock));

    FILE *file = fopen("log.txt","a+");
    char str[20] = "hello\n";
    fwrite(asctime(tblock), 1, strlen(asctime(tblock)), file);
    fwrite(str, 1, strlen(str), file);

    char tmp[2][5];
    char tmp1[5] = "10GE";
    char tmp2[5] = "sdh";
    char enter = '\n';
    char table = '\t';
    //printf("length is: %zd\n", strlen(enter));
    //printf("size is: %zd\n", sizeof(enter));
    strcpy(tmp[0], tmp1);
    strcpy(tmp[1], tmp2);
    fwrite(tmp[0], 1, strlen(tmp[0]), file);
    //fwrite(table, 1, strlen(table), file);
    fputc(table, file);
    fwrite(tmp[1], 1, strlen(tmp[0]), file);
    //fwrite(enter, 1, strlen(enter), file);
    fputc(enter, file);

    //fflush(file);
    fclose(file);
    return 0;
}
