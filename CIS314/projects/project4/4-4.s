	.file	"4-4.c"
	.text
	.globl	transpose
	.type	transpose, @function
transpose:
.LFB11:
	.cfi_startproc
	movl	$0, %r8d
	jmp	.L2
.L4:
	movq	(%rax), %rcx
	movq	(%rdx), %rsi
	movq	%rsi, (%rax)
	movq	%rcx, (%rdx)
	addq	$8, %rax
	addq	$32, %rdx
.L3:
	cmpq	%rdx, %rax
	jne	.L4
	addq	$1, %r8
.L2:
	cmpq	$3, %r8
	jg	.L6
	movq	%r8, %rax
	salq	$5, %rax
	addq	%rdi, %rax
	leaq	(%rdi,%r8,8), %rdx
	jmp	.L3
.L6:
	ret
	.cfi_endproc
.LFE11:
	.size	transpose, .-transpose
	.section	.rodata.str1.1,"aMS",@progbits,1
.LC0:
	.string	"%ld "
	.text
	.globl	main
	.type	main, @function
main:
.LFB12:
	.cfi_startproc
	pushq	%rbp
	.cfi_def_cfa_offset 16
	.cfi_offset 6, -16
	pushq	%rbx
	.cfi_def_cfa_offset 24
	.cfi_offset 3, -24
	subq	$152, %rsp
	.cfi_def_cfa_offset 176
	movq	%fs:40, %rax
	movq	%rax, 136(%rsp)
	xorl	%eax, %eax
	movq	$1, (%rsp)
	movq	$2, 8(%rsp)
	movq	$3, 16(%rsp)
	movq	$4, 24(%rsp)
	movq	$5, 32(%rsp)
	movq	$6, 40(%rsp)
	movq	$7, 48(%rsp)
	movq	$8, 56(%rsp)
	movq	$9, 64(%rsp)
	movq	$10, 72(%rsp)
	movq	$11, 80(%rsp)
	movq	$12, 88(%rsp)
	movq	$13, 96(%rsp)
	movq	$14, 104(%rsp)
	movq	$15, 112(%rsp)
	movq	$16, 120(%rsp)
	movq	%rsp, %rdi
	call	transpose
	movl	$0, %ebp
	jmp	.L8
.L9:
	leaq	(%rbx,%rbp,4), %rax
	movq	(%rsp,%rax,8), %rsi
	leaq	.LC0(%rip), %rdi
	movl	$0, %eax
	call	printf@PLT
	addq	$1, %rbx
.L10:
	cmpq	$3, %rbx
	jle	.L9
	movl	$10, %edi
	call	putchar@PLT
	addq	$1, %rbp
.L8:
	cmpq	$3, %rbp
	jg	.L14
	movl	$0, %ebx
	jmp	.L10
.L14:
	movq	136(%rsp), %rax
	xorq	%fs:40, %rax
	jne	.L15
	movl	$0, %eax
	addq	$152, %rsp
	.cfi_remember_state
	.cfi_def_cfa_offset 24
	popq	%rbx
	.cfi_def_cfa_offset 16
	popq	%rbp
	.cfi_def_cfa_offset 8
	ret
.L15:
	.cfi_restore_state
	call	__stack_chk_fail@PLT
	.cfi_endproc
.LFE12:
	.size	main, .-main
	.ident	"GCC: (Arch Linux 9.3.0-1) 9.3.0"
	.section	.note.GNU-stack,"",@progbits
