	.file	"4-1.c"
	.text
	.globl	loop
	.type	loop, @function
loop:
.LFB11:
	.cfi_startproc
	movq	%rsi, %rcx
	movl	$1, %eax
	movl	$0, %edx
	jmp	.L2
.L3:
	movq	%rax, %rsi
	andq	%rdi, %rsi
	orq	%rsi, %rdx
	salq	%cl, %rax
.L2:
	testq	%rax, %rax
	jne	.L3
	movq	%rdx, %rax
	ret
	.cfi_endproc
.LFE11:
	.size	loop, .-loop
	.section	.rodata.str1.1,"aMS",@progbits,1
.LC0:
	.string	"%ld\n"
	.text
	.globl	main
	.type	main, @function
main:
.LFB12:
	.cfi_startproc
	subq	$8, %rsp
	.cfi_def_cfa_offset 16
	movl	$5, %esi
	movl	$1, %edi
	call	loop
	movq	%rax, %rsi
	leaq	.LC0(%rip), %rdi
	movl	$0, %eax
	call	printf@PLT
	movl	$4, %esi
	movl	$2, %edi
	call	loop
	movq	%rax, %rsi
	leaq	.LC0(%rip), %rdi
	movl	$0, %eax
	call	printf@PLT
	movl	$3, %esi
	movl	$3, %edi
	call	loop
	movq	%rax, %rsi
	leaq	.LC0(%rip), %rdi
	movl	$0, %eax
	call	printf@PLT
	movl	$2, %esi
	movl	$4, %edi
	call	loop
	movq	%rax, %rsi
	leaq	.LC0(%rip), %rdi
	movl	$0, %eax
	call	printf@PLT
	movl	$1, %esi
	movl	$5, %edi
	call	loop
	movq	%rax, %rsi
	leaq	.LC0(%rip), %rdi
	movl	$0, %eax
	call	printf@PLT
	movl	$0, %eax
	addq	$8, %rsp
	.cfi_def_cfa_offset 8
	ret
	.cfi_endproc
.LFE12:
	.size	main, .-main
	.ident	"GCC: (GNU) 10.2.0"
	.section	.note.GNU-stack,"",@progbits
