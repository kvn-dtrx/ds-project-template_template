# ---
# description: Configuration for notebooks.
# ---

# Required imports

import os
import subprocess
import matplotlib.pyplot as plt
from typing import Any, Dict

# ---

# General configurations

# Configuration dictionary to hold various settings.
CFG: Dict[str, Any] = {}

# Random seed for reproducibility.
CFG["RSEED"] = 42

# Root directory of the project.
CFG["ROOT_DIR"] = subprocess.run(
    ["git", "rev-parse", "--show-toplevel"],
    capture_output=True,
    text=True,
).stdout.strip()


# Function to join tokens with a root directory.
def join_with_root(*tokens: str, root: str = CFG["ROOT_DIR"]) -> str:
    path = os.path.join(root, *tokens)
    return path


# Directory for storing data, plots, and source code.
CFG["DATA_DIR"] = join_with_root("data")
CFG["PLOTS_DIR"] = join_with_root("plots")
CFG["SRC_DIR"] = join_with_root("src")

# ---

# Matplotlib style

# Basic matplotlib style settings
# PLT_STYLE = "seaborn-v0_8-darkgrid"
# PLT_STYLE = "fast"
PLT_STYLE = "dark_background"

try:
    plt.style.use(PLT_STYLE)
except:
    print("Could not load the specified matplotlib style:")
    print(PLT_STYLE)
    print("Default style will be used")

plt.rcParams["axes.titleweight"] = "bold"
plt.rcParams["axes.titlesize"] = 18
plt.rcParams["axes.labelsize"] = 12
plt.rcParams["axes.labelweight"] = "bold"
# plt.rcParams["axes.labelcolor"] = "white"

plt.rcParams["figure.dpi"] = 600
plt.rcParams["figure.figsize"] = (10, 5)
plt.rcParams["savefig.format"] = "svg"
plt.rcParams["savefig.dpi"] = 600

plt.rcParams["grid.color"] = "gray"
plt.rcParams["grid.linestyle"] = "--"

plt.rcParams["xtick.labelsize"] = 10
plt.rcParams["ytick.labelsize"] = 10
plt.rcParams["xtick.direction"] = "in"
plt.rcParams["ytick.direction"] = "in"

plt.rcParams["legend.loc"] = "upper right"
plt.rcParams["legend.frameon"] = False

plt.rcParams["lines.linewidth"] = 2
plt.rcParams["lines.markersize"] = 8
