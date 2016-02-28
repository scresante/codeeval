#include <stdio.h>
#include <stdlib.h>
int main(int argc, const char * argv[]) {
    FILE *file = fopen(argv[1], "r");
    char line[1024];
    int num;
    char * pEnd;
    while (fgets(line, 1024, file)) {
      num = strtol(line,&pEnd,16);
      printf ("%d\n", num);
        // Do something with the line
    }
    return 0;
}
