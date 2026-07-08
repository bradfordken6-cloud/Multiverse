#include "kernel.h"

// Kernel entry point
void kmain(void) {
    // Initialize screen
    init_screen();
    
    // Print welcome message
    print("KenJoe Operating System v1.0\n");
    print("Initializing kernel...\n");
    
    // Initialize interrupts
    init_interrupts();
    
    // Initialize memory management
    init_memory();
    
    print("Kernel initialized successfully!\n");
    
    // Main loop
    while (1) {
        asm volatile("hlt");
    }
}

// Screen initialization
void init_screen(void) {
    // Clear video memory
    unsigned char *vram = (unsigned char *)0xB8000;
    for (int i = 0; i < 80 * 25 * 2; i += 2) {
        vram[i] = ' ';
        vram[i + 1] = 0x07; // White on black
    }
}

// Print string to screen
void print(const char *str) {
    static unsigned int x = 0, y = 0;
    unsigned char *vram = (unsigned char *)0xB8000;
    
    while (*str) {
        if (*str == '\n') {
            x = 0;
            y++;
        } else {
            vram[(y * 80 + x) * 2] = *str;
            vram[(y * 80 + x) * 2 + 1] = 0x07;
            x++;
            if (x >= 80) {
                x = 0;
                y++;
            }
        }
        str++;
    }
}
