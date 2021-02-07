	.file	"4-4.c"
	.text
	.globl	transpose
	.type	transpose, @function
transpose:
.LFB0:
	.cfi_startproc
	movq	%rdi, %r9
	movl	$0, %esi
	jmp	.L2
.L4:
	movq	(%rax), %rdi
	movq	(%rdx), %r8
	movq	%r8, (%rax)
	movq	%rdi, (%rdx)
	addq	$64, %rax
	addq	$256, %rdx
	addq	$1, %rcx
.L3:
	cmpq	%rcx, %rsi
	jg	.L4
	addq	$1, %rsi
.L2:
	cmpq	$3, %rsi
	jg	.L6
	movq	%rsi, %rax
	salq	$5, %rax
	addq	%r9, %rax
	leaq	(%r9,%rsi,8), %rdx
	movl	$0, %ecx
	jmp	.L3
.L6:
	ret
	.cfi_endproc
.LFE0:
	.size	transpose, .-transpose
	.globl	main
	.type	main, @function
main:
.LFB1:
	.cfi_startproc
	subq	$152, %rsp
	.cfi_def_cfa_offset 160
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
	movq	136(%rsp), %rax
	subq	%fs:40, %rax
	jne	.L10
	movl	$0, %eax
	addq	$152, %rsp
	.cfi_remember_state
	.cfi_def_cfa_offset 8
	ret
.L10:
	.cfi_restore_state
	call	__stack_chk_fail@PLT
	.cfi_endproc
.LFE1:
	.size	main, .-main
	.ident	"GCC: (GNU) 10.2.0"
	.section	.note.GNU-stack,"",@progbits
