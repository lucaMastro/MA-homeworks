#include <stdio.h>
#include <math.h>

void main(){
	long i, rest, test;
	long range = pow(2,32);
	for (i = 0; i < range; i++){
		rest = i % 4;
		test = i & 3;
		if (rest != test)
			printf("i = %ld\n", i);
	}
}
