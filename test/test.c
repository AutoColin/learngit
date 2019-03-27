#include <stdio.h>
#include <string.h>
/*struct
{
	unsigned int a;
	unsigned int b;
}status1;

struct
{
	unsigned int a:1;
	unsigned int b:1;
}status2;

int main(void)
{
	printf("Memory size occupied by status1: %d\n",sizeof(status1));
	
	printf("Memory size occupied by status2: %d\n",sizeof(status2));
	printf("hello,world\n");
	return 0;
}*/
int test();

int main(void)
{
	unsigned int a = 0xc305ad3;
	a |= (1<<3);
	printf("a = 0x%x.\n",a);
	test();
	return 0;
}

int test()
{
	printf("success 1  2   3   4 \n");
	printf("success 1  2  \r 3   4\n");
	printf("success 1  2  \r\n 3   4 \n");
	printf("success 1  2  \n 3   4 \n");
	return 0;
}
