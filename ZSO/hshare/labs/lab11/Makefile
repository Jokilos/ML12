CC=gcc 
CFLAGS=-g -O0 -Wall
CFLAGS=-g -O0 -Wall -fno-stack-protector
LD=gcc
LDFLAGS= -Wall -z execstack
LDFLAGS= -Wall
OBJDUMP=objdump -d
AS=as
ASFLAGS=
PAGER?=less


all: server payload exec demo gadgets.o

payload.o: payload.s
	${AS} ${ASFLAGS} -o payload.o payload.s

exec: exec.o
	${LD} ${LDFLAGS} -o exec -static exec.o

vdso: dump_vdso
	./dump_vdso '[vdso]' > vdso

show-vdso: vdso
	@ ${OBJDUMP} vdso

vsyscall: dump_vdso
	./dump_vdso '[vsyscall]' > vsyscall

show-vsyscall: vsyscall
	@ ${OBJDUMP} vsyscall

login: login.o
	${LD} ${LDFLAGS} -o login login.o -lssl -lcrypto

clean:
	rm -f server payload exec demo dump_vdso *.o vdso login

show-payload: payload.o
	@ echo Payload:
	@ ${OBJDUMP} payload.o | grep "[0-9a-f]:" | cut -f 2 | tr "\n\t" " " | tr -s " " | sed "s/\([0-9a-f][0-9a-f]*\)/0x\1/g" | sed "s/ \([0-9a-f]\)/, \1/g"
	@ echo

show-exec: exec
	@ ${OBJDUMP} exec | ${PAGER}
