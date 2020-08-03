#include <stdio.h>
#include <malloc.h>
#include <stdlib.h>

int main(void){
	int data1, data2;
	char *string;
	string = malloc(_MAX_PATH);
	
	printf("Enter number: ");
	scanf("%d", data1);
	printf("Your number: %d", data1);
	
	printf("Enter dotted number: ");
	scanf("%f", data2);
	printf("Your number: %.2f", data2);
	
	printf("Enter string: ");
	gets(string);
	printf("Your string: %s", string);
	
	free(string);
	return 0;
}