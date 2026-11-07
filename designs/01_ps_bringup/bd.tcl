# designs/01_ps_bringup/bd.tcl — PS-only block design
# Hand-written while the design is small; larger GUI-edited designs get exported with write_bd_tcl.

create_bd_design "system"

set ps [create_bd_cell -type ip -vlnv xilinx.com:ip:processing_system7 ps7]

# Board preset configures DDR3, MIO (UART, SD, USB, Ethernet) and clocks for the Cora
apply_bd_automation -rule xilinx.com:bd_rule:processing_system7 \
    -config {make_external "FIXED_IO, DDR" apply_board_preset "1" Master "Disable" Slave "Disable"} $ps

# No PL peripherals yet: disable the GP0 master so it doesn't need a clock connected
set_property CONFIG.PCW_USE_M_AXI_GP0 {0} $ps

validate_bd_design
save_bd_design
