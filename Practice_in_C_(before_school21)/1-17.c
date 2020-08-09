/* Напишите функцию REVERSE(S), которая распологает символьную строку S в
обратном порядке. С ее помощью напишите программу, которая обратит каждую
строку из файла ввода. */


#include <stdio.h>
#include <stdlib.h>
#include <malloc.h>

char * reverse(char * s) {
	
	int len_str = 0;
	char symbol;
	
	while (s[len_str] != '\0'){
		len_str += 1;
	}

	for (int i = 0; i<len_str/2; ++i){
		symbol = s[i];
		s[i] = s[len_str - 1 - i];
		s[len_str - 1 - i] = symbol;
	}
	
	return s;
}


int main(){
	
	int count = 0;
	char * string;
	int max_count = 5;
	string = (char *)malloc(sizeof(char)*max_count);
	
	char symbol = 0;
	while (symbol != '\n') {
		symbol = getc(stdin);
		string[count] = symbol;
		count += 1;
		
		if (count == max_count) {
			max_count *= 2;
			char * string_new;
			string_new = (char *)malloc(sizeof(char)*max_count);
			
			for (int i = 0; i<count; ++i){
				string_new[i] = string[i];
			}
			
			free(string);
			string = string_new;
		}
	}
	
	printf("Reverse string: %s\n", reverse(string));
	
	free(string);

	return 0;
}