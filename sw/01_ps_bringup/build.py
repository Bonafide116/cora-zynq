# sw/01_ps_bringup/build.py
# Run from the repo root:  vitis -s sw/01_ps_bringup/build.py
#
# Creates a standalone (bare-metal) platform from the stage-01 .xsa, builds an
# app from src/, and writes a run.tcl for xsdb next to the workspace.

import os
import shutil
import vitis

DESIGN = "01_ps_bringup"
here = os.path.dirname(os.path.abspath(__file__))
repo = os.path.abspath(os.path.join(here, "..", ".."))
build = os.path.join(repo, "build", DESIGN)
xsa = os.path.join(build, "system.xsa")
ws = os.path.join(build, "vitis")
src = os.path.join(here, "src")

if not os.path.isfile(xsa):
    raise SystemExit(f"Missing {xsa}; run designs/{DESIGN}/build.tcl first")

# Fresh workspace every time: nothing in it is source
shutil.rmtree(ws, ignore_errors=True)

client = vitis.create_client()
client.set_workspace(path=ws)

# --- Platform: hardware handoff + standalone BSP for CPU0 -------------------
platform = client.create_platform_component(
    name="cora_plat",
    hw_design=xsa,
    os="standalone",
    cpu="ps7_cortexa9_0",
    domain_name="standalone_a9_0",
)
platform.build()
xpfm = client.find_platform_in_repos("cora_plat")

# --- Application: empty template + our sources ------------------------------
app = client.create_app_component(
    name="hello",
    platform=xpfm,
    domain="standalone_a9_0",
    template="empty_application",
)
app.import_files(
    from_loc=src,
    files=[f for f in os.listdir(src) if f.endswith((".c", ".h"))],
    dest_dir_in_cmp="src",
)
app.build()


# --- Generate an xsdb run script with absolute paths ------------------------
def find(name, root):
    for d, _, files in os.walk(root):
        if name in files:
            return os.path.join(d, name)
    raise SystemExit(f"Could not find {name} under {root}")

ps7_init = find("ps7_init.tcl", os.path.join(ws, "cora_plat"))
elf = find("hello.elf", os.path.join(ws, "hello"))

run_tcl = os.path.join(build, "run.tcl")
with open(run_tcl, "w") as f:
    f.write(f"""connect
targets -set -nocase -filter {{name =~ "APU*"}}
rst -system
after 1000
targets -set -nocase -filter {{name =~ "*cortex-a9*#0"}}
source {{{ps7_init}}}
ps7_init
ps7_post_config
dow {{{elf}}}
con
""")

print(f"\n*** Built {elf}\n*** Run with: xsdb {run_tcl}\n")
vitis.dispose()
