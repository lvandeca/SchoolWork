	.file	"3-2.c"
	.text
	.globl	f
	.type	f, @function
f:
.LFB23:
	.cfi_startproc
	endbr64
	addq	%rsi, %rdx
	imulq	%rdx, %rdi
	salq	$63, %rdx
	sarq	$63, %rdx
	movq	%rdi, %rax
	xorq	%rdx, %rax
	ret
	.cfi_endproc
.LFE23:
	.size	f, .-f
	.section	.rodata.str1.1,"aMS",@progbits,1
.LC0:
	.string	"%ld\n"
	.text
	.globl	main
	.type	main, @function
main:
.LFB24:
	.cfi_startproc
	endbr64
	subq	$8, %rsp
	.cfi_def_cfa_offset 16
	movl	$4, %edx
	movl	$2, %esi
	movl	$1, %edi
	call	f
	movq	%rax, %rdx
	leaq	.LC0(%rip), %rsi
	movl	$1, %edi
	movl	$0, %eax
	call	__printf_chk@PLT
	movl	$7, %edx
	movl	$5, %esi
	movl	$3, %edi
	call	f
	movq	%rax, %rdx
	leaq	.LC0(%rip), %rsi
	movl	$1, %edi
	movl	$0, %eax
	call	__printf_chk@PLT
	movl	$30, %edx
	movl	$20, %esi
	movl	$10, %edi
	call	f
	movq	%rax, %rdx
	leaq	.LC0(%rip), %rsi
	movl	$1, %edi
	movl	$0, %eax
	call	__printf_chk@PLT
	movl	$0, %eax
	addq	$8, %rsp
	.cfi_def_cfa_offset 8
	ret
	.cfi_endproc
.LFE24:
	.size	main, .-main
	.ident	"GCC: (Ubuntu 9.3.0-17ubuntu1~20.04) 9.3.0"
	.section	.note.GNU-stack,"",@progbits
	.section	.note.gnu.property,"a"
	.align 8
	.long	 1f - 0f
	.long	 4f - 1f
	.long	 5
0:
	.string	 "GNU"
1:
	.align 8
	.long	 0xc0000002
	.long	 3f - 2f
2:
	.long	 0x3
3:
	.align 8
4:
