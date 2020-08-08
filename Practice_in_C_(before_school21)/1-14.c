/* Переделайте ведущую часть программы поиска самой длинной строки таким
образом, чтобы она правильно печатала длины сколь угодно длинных вводимых строк
и возможно больший текст. */


#include <stdio.h>
#include <malloc.h>
#include <stdlib.h>

int main(void){

	int result_count, count = 0;
	int max_count = 5;
	char * result_string = 0;
	char * memory;
	memory = (char *)malloc(sizeof(char)*max_count);
	
	do {
		char symbol = 0;
		count = 0;
		while (symbol != '\n') {
			symbol = getc(stdin);
			memory[count] = symbol;
			count += 1;
			
			if (count == max_count) {
				max_count *= 2;
				char * memory_new;
				memory_new = (char *)malloc(sizeof(memory_new)*max_count);
				
				for (int i = 0; i<count; ++i){
					memory_new[i] = memory[i];
				}
				
				free(memory);
				memory = memory_new;
			}
		}
		if (count > result_count){
			result_count = count - 1;
			free(result_string);
			result_string = memory;
			memory = (char *)malloc(sizeof(char)*max_count);
		}
	} while (count != 1);

	printf("Count: %d \nString: %s \n", result_count, result_string);
	
	free(result_string);
	free(memory);
	
	return 0;
}