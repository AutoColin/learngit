#include <stdio.h>

#define SET_BIT(x,n) (x | 1U<<(n-1))

int main(void)
{
	unsigned int a = 0;
	unsigned int b = 0;
	
	b = SET_BIT(a,4);
	printf("b = 0x%x.\n", b);
 	return 0;
}
