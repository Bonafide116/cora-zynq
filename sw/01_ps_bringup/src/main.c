// sw/01_ps_bringup/src/main.c — bare-metal bring-up on the Cora Z7 PS
#include <stdint.h>
#include "xil_printf.h"
#include "sleep.h"

// MPIDR: Multiprocessor Affinity Register. Bits [1:0] = which A9 core we're on.
static inline uint32_t read_mpidr(void)
{
    uint32_t v;
    __asm__ volatile("mrc p15, 0, %0, c0, c0, 5" : "=r"(v));
    return v;
}

// SLCR PSS_IDCODE (0xF8000530): identifies the exact Zynq device the PS is in.
#define SLCR_PSS_IDCODE (*(volatile uint32_t *)0xF8000530u)

int main(void)
{
    uint32_t mpidr = read_mpidr();
    uint32_t idcode = SLCR_PSS_IDCODE;

    xil_printf("\r\n=== Cora Z7 PS bring-up ===\r\n");
    xil_printf("Running on Cortex-A9 core %d (MPIDR=0x%08x)\r\n",
               (int)(mpidr & 0x3), (unsigned)mpidr);
    xil_printf("PSS_IDCODE = 0x%08x (device code 0x%02x)\r\n",
               (unsigned)idcode, (unsigned)((idcode >> 12) & 0x1F));

    for (uint32_t t = 0;; t++) {
        xil_printf("uptime %u s\r\n", (unsigned)t);
        sleep(1);
    }
    return 0;
}
