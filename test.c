#include <stdio.h>
#include <string.h>

static char s[] = "had";
static char *s_ptr = s;

int main()
{
    char str[] = "hello";
    printf("%s world\n", str);
    strcpy(str, "hell");
    printf("%s\n", str);

    printf("%s\n", s_ptr);
    strcpy(s_ptr, "hasabcde");
    printf("%s\n", s_ptr);
}
