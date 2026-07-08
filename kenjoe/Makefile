.PHONY: build run clean

CC = gcc
AS = as
LD = ld
CFLAGS = -Wall -Wextra -std=c99 -ffreestanding
ASFLAGS = 
LDFLAGS = -T linker.ld

SRCS = kernel/main.c kernel/interrupt.c kernel/memory.c
OBJS = $(SRCS:.c=.o) bootloader/boot.o
TARGET = kenjoe.bin

build: $(TARGET)

$(TARGET): $(OBJS)
	$(LD) $(LDFLAGS) -o $@ $^

%.o: %.c
	$(CC) $(CFLAGS) -c $< -o $@

%.o: %.s
	$(AS) $(ASFLAGS) $< -o $@

run: build
	qemu-system-x86_64 -kernel $(TARGET)

clean:
	rm -f $(OBJS) $(TARGET)
