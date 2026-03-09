#include <stdio.h>
#include <stdlib.h>
int main(int argc, char *argv[]) {
    int n = atoi(argv[1]), sum = 0;
    for(int i=1;i<=n;i++)
        sum += i;
    printf("Sum of first %d natural numbers: %d\n", n, sum);
    return 0;
}
