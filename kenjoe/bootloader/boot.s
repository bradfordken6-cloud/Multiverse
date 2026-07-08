; KenJoe Bootloader
; 32-bit protected mode bootloader

[BITS 16]
[ORG 0x7C00]

start:
    mov ax, 0x00
    mov ds, ax
    mov es, ax
    mov ss, ax
    mov sp, 0x7C00

    cli

    ; Load GDT
    lgdt [gdt_descriptor]

    ; Enter protected mode
    mov eax, cr0
    or eax, 0x1
    mov cr0, eax

    ; Far jump to 32-bit code
    jmp 0x08:start32

[BITS 32]
start32:
    ; Set up 32-bit segment registers
    mov ax, 0x10
    mov ds, ax
    mov es, ax
    mov ss, ax

    ; Jump to kernel
    extern kmain
    call kmain

    ; Halt
    hlt
    jmp $

; GDT Definition
gdt_start:
    dd 0x0
    dd 0x0

gdt_code:
    dw 0xFFFF
    dw 0x0
    db 0x0
    db 0x9A
    db 0xCF
    db 0x0

gdt_data:
    dw 0xFFFF
    dw 0x0
    db 0x0
    db 0x92
    db 0xCF
    db 0x0

gdt_end:

gdt_descriptor:
    dw gdt_end - gdt_start - 1
    dd gdt_start

; Boot signature
times 510 - ($ - $$) db 0
dw 0xAA55
