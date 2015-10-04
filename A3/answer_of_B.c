#include <stdio.h>
#define N 50

int map[] = {
	1, 2, 3,
	1, 2, 3,
	1, 2, 3,
	1, 2, 3,
	1, 2, 3,
	1, 2, 3, 4,
	1, 2, 3,
	1, 2, 3, 4
};

int main(int argc, char *argv[]) {
	char str[N + 1];
	char *strp = str;

	int index = 0;

	if (argc > 1)
		strp = argv[1];
	else
		fgets(strp, N, stdin);

	while (strp[index]) {
		printf("%c%d", strp[index], map[strp[index] - 'a']);
		index++;
	}

	printf("\n");
    return 0;
}
