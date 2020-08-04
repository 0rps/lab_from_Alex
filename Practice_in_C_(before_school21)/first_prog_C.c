#include <stdio.h>
#include <malloc.h>
#include <stdlib.h>

int main(void){
	int data1;
	float data2;
	char *string;
	string = (char*)malloc(_MAX_PATH);
	
	printf("Enter number: ");
	scanf("%d", &data1);
	printf("Your number: %d\n", data1);
	
	printf("Enter dotted number: ");
	scanf("%f", &data2);
	printf("Your number: %.2f\n", data2);
	
	char c = getc(stdin);
	while(c!=10)
	{
		c = getc(stdin);
	};

	printf("Enter string: ");
	gets(string);
	printf("Your string: %s", string);
	
	free(string);
	return 0;
}