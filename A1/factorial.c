#include <stdio.h>
#define N 5

enum model {
    multiplication,
    addition,
};

int calculate(enum model, int[], size_t);

int main(int argc, char *args[]) {
    int data[N] = {1, 2, 3, 4, 5};
    printf("multiplication: %d\n", calculate(multiplication, data, N));
    printf("addition: %d\n", calculate(addition, data, N));
    return 0;
}

int calculate(enum model flag, int data[], size_t end) {
	int ans;
	switch (flag) {
		case multiplication:
			ans = 1;
			for (int i = 0; i < end; i++)
				ans *= data[i];
			break;

		case addition:
			ans = 0;
			for (int i = 0; i < end; i++)
				ans += data[i];
			break;

		default:
			break;
	}
    return ans;
}
