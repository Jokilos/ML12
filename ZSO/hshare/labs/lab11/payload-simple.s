.text

main:
	pushq %rbp
	movq %rsp, %rbp

	/* prepare arguments */
	mov $0x0068732f,%rax
    shl  $32, %rax
	or $0x6e69622f,%rax /*/bin/sh*/
    push %rax
	push $0
	push %rsp

	/* push execve arguments on stack */	
	lea -8(%rbp), %rdi /*/bin/sh*/
	lea -16(%rbp), %rsi /*ptr to NULL*/
	lea -24(%rbp), %rdx /*ptr to /bin/sh and then NULL*/

	/*call execve*/
	movl $59, %eax /*mark execve syscall*/
	syscall /*make the syscall*/

	/*not reached*/
	
.global main
