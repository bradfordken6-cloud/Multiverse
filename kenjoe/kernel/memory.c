#include "kernel.h"

#define KERNEL_HEAP_SIZE 1024 * 1024 // 1MB

// Simple memory allocator
static uint8_t kernel_heap[KERNEL_HEAP_SIZE];
static size_t heap_ptr = 0;

// Initialize memory management
void init_memory(void) {
    heap_ptr = 0;
    print("Memory management initialized\n");
}

// Simple malloc implementation
void *malloc(size_t size) {
    if (heap_ptr + size > KERNEL_HEAP_SIZE) {
        return NULL; // Out of memory
    }
    
    void *ptr = &kernel_heap[heap_ptr];
    heap_ptr += size;
    return ptr;
}

// Simple free implementation (no-op for now)
void free(void *ptr) {
    // Placeholder
}
