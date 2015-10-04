#include <stdio.h>
int main(int argc, char *argv[]) {
    int num;
    scanf("%d", &num);

    int count = 0;
    do 
       count++;
    while (num /= 10);

    printf("The sum digital is %d\n", count);
    return 0;
}
