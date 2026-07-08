#ifndef KERNEL_H
#define KERNEL_H

#include <stddef.h>
#include <stdint.h>

// Function prototypes
void kmain(void);
void init_screen(void);
void print(const char *str);
void init_interrupts(void);
void init_memory(void);

#endif // KERNEL_H
