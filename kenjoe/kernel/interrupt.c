#include "kernel.h"

// IDT (Interrupt Descriptor Table) structure
struct idt_entry {
    uint16_t base_lo;
    uint16_t sel;
    uint8_t always0;
    uint8_t flags;
    uint16_t base_hi;
} __attribute__((packed));

struct idt_ptr {
    uint16_t limit;
    uint32_t base;
} __attribute__((packed));

// IDT array
struct idt_entry idt[256];
struct idt_ptr idtp;

// Initialize interrupts
void init_interrupts(void) {
    idtp.limit = (sizeof(struct idt_entry) * 256) - 1;
    idtp.base = (uint32_t)&idt;
    
    print("Interrupts initialized\n");
}

// Interrupt handler stub
void isr_handler(uint32_t int_no) {
    print("Interrupt received: ");
    // Would print interrupt number here
}
