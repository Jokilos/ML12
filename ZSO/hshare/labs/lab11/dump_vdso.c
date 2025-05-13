#include <stdio.h>
#include <unistd.h>
#include <fcntl.h>
#include <string.h>

int main(int argc, char **argv)
{
#define LINE_LEN 256
	char line[LINE_LEN];
	FILE *maps = fopen("/proc/self/maps", "r");
	if (!maps) {
		perror("fopen");
		return 1;
	}

    if (argc < 2) {
        fprintf(stderr, "Usage: %s <map-name>\n", argv[0]);
        return 1;
    }

	while (fgets(line, LINE_LEN, maps)) {
		if (strstr(line, argv[1])) {
			unsigned long addr1,addr2;
			int err;
			err = sscanf(line, "%lx-%lx", &addr1, &addr2);
			if (err != 2) {
				fprintf(stderr, "Unexpected format: %s\n", line);
				return 1;
			}
			while (addr1 != addr2) {
				err = write(1, (char*)addr1, 4096);
				if (err != 4096) {
					if (err >= 0)
						fprintf(stderr, "write: short write (%d)\n", err);
					else
						perror("write");
					return 1;
				}
				addr1 += 4096;
			}
			return 0;
		}
	}
	fprintf(stderr, "No vdso-related line found!");
	return 1;
}
