#-----------------------------------------------------------------
# Vitis v2026.1 (64-bit)
# Start of session at: Sat Oct 31 18:08:29 2026
# Current directory: /home/bona/Documents/Projects/fpga/cora-zynq
# Command line: vitis -i
# Journal file: vitis_journal.py
# Batch mode: $XILINX_VITIS/bin/vitis -s /home/bona/Documents/Projects/fpga/cora-zynq/vitis_journal.py
#-----------------------------------------------------------------

#!/usr/bin/env python3
import vitis
import vitis
c = vitis.create_client()
c.set_workspace(path="/home/bona/Documents/Projects/fpga/cora-zynq/build/01_ps_bringup/vitis_dbg")
#[Out]# True
p = c.create_platform_component(name="dbgplat", hw_design="/home/bona/Documents/Projects/fpga/cora-zynq/build/01_ps_bringup/system.xsa", os="standalone", cpu="ps7_cortexa9_0")
p = c.create_platform_component(name="dbgplat2", hw_design="/home/bona/Documents/Projects/fpga/cora-zynq/build/01_ps_bringup/system.xsa", os="standalone", cpu="ps7_cortexa9_0", no_boot_bsp=True)
p = c.create_platform_component(name="dbgplat2", hw_design="/home/bona/Documents/Projects/fpga/cora-zynq/build/01_ps_bringup/system.xsa", os="standalone", cpu="ps7_cortexa9_0", no_boot_bsp=True)
exit()
vitis.dispose()
