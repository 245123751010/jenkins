#include <stdio.h>
#include <stdlib.h>
int main(int argc, char *argv[]) {
    int n = atoi(argv[1]);
    if(n % 2 == 0) printf("%d is Even\n", n);
    else printf("%d is Odd\n", n);
    return 0;
}
