#include <stdio.h>
#include <unistd.h>

int test()
{
	char buf[128];
	if (scanf("%s", buf) == EOF)
        return 0;
    printf(buf);
    return 1;
}

int main()
{
	while (test()) {
		fflush(stdout);
    }
	return 0;
}

