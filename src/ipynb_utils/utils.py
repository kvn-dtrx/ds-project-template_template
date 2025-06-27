# ---
# description: Utility functions for notebooks.
# ---

import os
import pandas as pd
from typing import List
import matplotlib.pyplot as plt
from ipynb_nbutils.cfg import CFG


def dump_df(
    df: pd.DataFrame,
    core: str,
    extensions: List[str] = ["pkl"],
    dir: str = CFG["DATA_DIR"],
) -> None:
    for extension in extensions:
        target_path = os.path.join(dir, f"{core}.{extension}")
        if extension == "pkl":
            df.to_pickle(target_path)
        elif extension == "csv":
            df.to_csv(target_path, index=False)
        else:
            raise ValueError(f"Unsupported file extension: {extension}")


def load_data(
    name: str,
    dir: str = CFG["DATA_DIR"],
) -> pd.DataFrame:
    """_summary_

    Args:
        name (str): _description_
        dir (str, optional): _description_. Defaults to CFG["DATA_DIR"].

    Raises:
        ValueError: _description_

    Returns:
        pd.DataFrame: _description_
    """
    _, extension_ = os.path.splitext(name)
    extension = extension_.lstrip(".")
    target_path = os.path.join(dir, f"{name}")
    if extension == "pkl":
        return pd.read_pickle(target_path)
    elif extension == "csv":
        return pd.read_csv(target_path)
    else:
        raise ValueError(f"Unsupported file extension: {extension}")


def show_and_save_plot(
    save_path: str = None,
    dpi: int = 300,
    bbox_inches: str = "tight",
):
    """
    Display the current matplotlib plot and optionally save it.

    Args:
        save_path (str, optional): File path to save the plot (e.g., "plot.png").
        dpi (int): Resolution of saved image.
        bbox_inches (str): Bounding box option for saving. Use 'tight' to avoid extra whitespace.
    """
    if save_path:
        plt.savefig(save_path, dpi=dpi, bbox_inches=bbox_inches)
        print(f"Plot saved to: {save_path}")
    plt.show()
    plt.clf()  # Clear the current figure to prevent overlay in later plots


def get_alchemy_db_string(
    user: str,
    password: str,
    host: str,
    port: str,
    database: str,
) -> str:
    db_string = f"postgresql://{user}:{password}@{host}:{port}/{database}"
    return db_string

