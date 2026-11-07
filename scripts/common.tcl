# scripts/common.tcl — shared settings, sourced by every designs/*/build.tcl

set repo_root [file normalize [file join [file dirname [info script]] ..]]

# Set to match the part shown in Hardware Manager: "07s" (xc7z007s) or "10" (xc7z010)
set variant "07s"

switch -- $variant {
    07s { set part xc7z007sclg400-1 ; set board_glob "*cora-z7-07s*" }
    10  { set part xc7z010clg400-1  ; set board_glob "*cora-z7-10*"  }
    default { error "Unknown Cora variant '$variant'" }
}

# Parallel jobs for synth/impl runs
set jobs 8

# Pick the newest installed board-file revision matching the variant
proc resolve_board {glob} {
    set b [lindex [lsort [get_board_parts -quiet $glob]] end]
    if {$b eq ""} {
        error "No board files match '$glob'. Check board.repoPaths in ~/.Xilinx/Vivado/Vivado_init.tcl"
    }
    return $b
}
