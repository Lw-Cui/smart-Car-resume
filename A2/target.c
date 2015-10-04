#include "stdio.h"
#include "stdlib.h"

#define FIRST_SUBSCRIPT 0  
#define MAX_LEN 20
#define GET_ARRAY_LEN(array,len){len = (sizeof(array) / sizeof(array[0]));}

void func1(int array[],int i,int j);
void func2(int array[],int ii,int jj);
void func3(int *a,int *b);

int main(void)
{	
	int i;
	int array[15] = {45, 68, 12, 32, 7, 85, 456, 258, 128, 357, 4, 62, 62, 67, 29};
	int len;
	GET_ARRAY_LEN(array,len);
	if(len<=MAX_LEN)
        func1(array,FIRST_SUBSCRIPT,FIRST_SUBSCRIPT+len-1);
    else
        func2(array,FIRST_SUBSCRIPT,FIRST_SUBSCRIPT+len-1);
    printf("the sorted numbers:\n");
    for(i = FIRST_SUBSCRIPT; i < len; i++)
        printf("%5d",array[i]);   
    
	system("pause");
	return 0;    
} 

void func1(int array[],int i,int j)
{	volatile int a=i,b=j;
	int base = array[i];
	while(a<b)
	{	
		while(base<array[b]&&a<b)  b--;
	    if(a<b)  array[a++] = array[b];	
		while(a<b&&base>=array[a]) a++;				
		if(a<b)  array[b--] = array[a];
    }
    array[a] = base;
    if(i<a)  func1(array,i,b-1);
	if(a<j)  func1(array,b+1,j);
		
}

void func2(int array[],int ii,int jj)
{
	int i,j;
	for(i = ii; i <= jj-1; i++)
		 for(j = i+1; j <= jj; j++)		
		 	if(array[i]>array[j])		 	
		 		func3(&array[i],&array[j]);	     
}

void func3(int *a,int *b)
{
  int c=*a;
  *a=*b;
  *b=c;
}
