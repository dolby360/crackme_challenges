	.arch armv8-a
	.file	"chall.c"
	.text
	.align	2
	.global	func1
	.type	func1, %function
func1:
    sub sp, sp, #16         ; Allocate 16 bytes of space on the stack
    str w0, [sp, 12]       ; Store the value of register w0 at [sp + 12]
    str w1, [sp, 8]        ; Store the value of register w1 at [sp + 8]
    ldr w1, [sp, 12]       ; Load the value at [sp + 12] into register w1
    ldr w0, [sp, 8]        ; Load the value at [sp + 8] into register w0
    cmp w1, w0             ; Compare w1 and w0
    bls .L2                ; Branch to label .L2 if w1 <= w0
    ldr w0, [sp, 12]       ; Load the value at [sp + 12] into register w0
    b .L3                  ; Unconditional branch to label .L3
.L2:
    ldr w0, [sp, 8]        ; Load the value at [sp + 8] into register w0
.L3:
    add sp, sp, 16         ; Deallocate the stack space (undo the earlier stack allocation)
    ret                    ; Return from the function
    .size func1, .-func1   ; Calculate the size of the func1 function
    .section .rodata
    .align 3
.LC0:
    .string "Result: %ld\n" ; Define a string in the read-only data section
    .text
    .align 2
    .global main
    .type main, %function   ; Declare the main function as a global function
main:
    stp     x29, x30, [sp, -48]!   ; Store the previous frame pointer (x29) and link register (x30)
                                    ; onto the stack and update the stack pointer (sp).

    add     x29, sp, 0            ; Set up the frame pointer (x29) by copying the current
                                    ; stack pointer (sp) value.

    str     x19, [sp, 16]         ; Store the value of x19 register onto the stack at an offset of 16 bytes.

    str     w0, [x29, 44]         ; Store the value of w0 (lower 32 bits of x0) into the current stack frame at an offset of 44 bytes
                                    ; from the frame pointer (x29).

    str     x1, [x29, 32]         ; Store the value of x1 into the current stack frame at an offset of 32 bytes
                                    ; from the frame pointer (x29).

    ldr     x0, [x29, 32]         ; Load the value from memory at an offset of 32 bytes from the frame pointer (x29) into x0.

    add     x0, x0, 8            ; Add 8 to the value in x0.

    ldr     x0, [x0]              ; Load the value pointed to by x0 into x0.

    bl      atoi                   ; Call the atoi function to convert the string in x0 to an integer.

    mov     w19, w0               ; Move the result of atoi to w19.

    ldr     x0, [x29, 32]         ; Load the value from memory at an offset of 32 bytes from the frame pointer (x29) into x0.

    add     x0, x0, 16           ; Add 16 to the value in x0.

    ldr     x0, [x0]              ; Load the value pointed to by x0 into x0.

    bl      atoi                   ; Call the atoi function again to convert the string in x0 to an integer.

    mov     w1, w0                ; Move the result of atoi to w1.

    mov     w0, w19               ; Move the original result of atoi (from x19) to w0.

    bl      func1                  ; Call the function func1.

    mov     w1, w0                ; Move the result of func1 to w1.

    adrp    x0, .LC0              ; Load the address of a format string into x0.
                                    ; This is a 64-bit address computation.

    add     x0, x0, :lo12:.LC0    ; Add the lower 12 bits of the format string's address to x0.
                                    ; This completes the 64-bit address calculation.

    bl      printf                ; Call the printf function to print a formatted string.

    mov     w0, 0                 ; Set w0 to 0.

    ldr     x19, [sp, 16]         ; Load the value from memory at an offset of 16 bytes from the stack pointer (sp) into x19.

    ldp     x29, x30, [sp], 48    ; Restore the previous frame pointer (x29) and link register (x30)
                                    ; from the stack and update the stack pointer (sp).

    ret                            ; Return from the main function.

.size   main, .-main                ; Calculate the size of the main function.

.ident  "GCC: (Ubuntu/Linaro 7.5.0-3ubuntu1~18.04) 7.5.0" ; Compiler version identification.

.section    .note.GNU-stack,"",@progbits  ; Section for stack behavior information.
