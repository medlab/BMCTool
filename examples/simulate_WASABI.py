"""
simulate_WASABI.py
    Script to run the BMCTool simulation for WASABI sequence.
"""
from pathlib import Path
from bmctool.bmc_tool import BMCTool
from bmctool.utils.eval import plot_z
from bmctool.set_params import load_params

# set necessary file paths:
config_file = Path(__file__).parent / 'library' / 'example_config.yaml'
seq_file = Path(__file__).parent / 'library' / 'WASABI.seq'

# load config file(s) and print settings
sim_params = load_params(config_file)
sim_params.print_settings()

# create BMCTool object and run simulation
sim = BMCTool(sim_params, seq_file)
sim.run()

# create BMCToll object and run simulation
Sim = BMCTool(sim_params, seq_file)
Sim.run()

# extract and plot z-spectrum
offsets, mz = sim.get_zspec()
fig = plot_z(mz=mz,
             offsets=offsets,
             invert_ax=True,
             plot_mtr_asym=False,
             title='Example WASABI spectrum')
