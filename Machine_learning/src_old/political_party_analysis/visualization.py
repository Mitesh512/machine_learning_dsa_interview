from itertools import cycle
from typing import List, Optional
from matplotlib.axes import Axes
import matplotlib as mpl
import numpy as np
import pandas as pd
from matplotlib import pyplot


def scatter_plot(
    transformed_data: pd.DataFrame,
    color: str = "y",
    size: float = 2.0,
    splot: Optional[Axes] = None,
    label: Optional[List[str]] = None,
):
    """Write a function to generate a 2D scatter plot."""
    if splot is None:
        splot = pyplot.subplot()
    columns = transformed_data.columns
    splot.scatter(
        transformed_data.loc[:, columns[0]],
        transformed_data.loc[:, columns[1]],
        size,
        c=color,
        label=label,
    )
    splot.set_aspect("equal", "box")
    splot.set_xlabel("1st Component")
    splot.set_ylabel("2nd Component")
    splot.legend()


def plot_density_estimation_results(
    X: pd.DataFrame,
    Y_: np.ndarray,
    means: np.ndarray,
    covariances: np.ndarray,
    title: str,
):
    """Use this function to plot the estimated distribution"""
    color_iter = cycle(["navy", "c", "cornflowerblue", "gold", "darkorange", "g"])
    pyplot.figure()
    splot = pyplot.subplot()
    for i, (mean, covar, color) in enumerate(zip(means, covariances, color_iter)):
        v, w = np.linalg.eigh(covar)
        v = 2.0 * np.sqrt(2.0) * np.sqrt(v)
        u = w[0] / np.linalg.norm(w[0])
        if not np.any(Y_ == i):
            continue
        scatter_plot(X.loc[Y_ == i], color=color, splot=splot)
        angle = np.arctan(u[1] / u[0])
        angle = 180.0 * angle / np.pi
        ell = mpl.patches.Ellipse(mean, v[0], v[1], angle=180.0 + angle, color=color)
        ell.set_clip_box(splot.bbox)
        ell.set_alpha(0.5)
        splot.add_artist(ell)
    pyplot.title(title)


def plot_finnish_parties(transformed_data: pd.DataFrame, splot: Optional[Axes] = None):
    finnish_parties = [
        {"parties": ["SDP", "VAS", "VIHR"], "country": 14, "color": "r"},
        {"parties": ["KESK", "KD"], "country": 14, "color": "g"},
        {"parties": ["KOK", "SFP"], "country": 14, "color": "b"},
        {"parties": ["PS"], "country": 14, "color": "k"},
    ]
    if not all(level in transformed_data.index.names for level in ["country", "party"]):
        print("Warning: 'country' and 'party' not in index. Cannot plot Finnish parties.")
        return

    if splot is None:
        fig, splot = pyplot.subplots(figsize=(8, 6))

    for party_group in finnish_parties:
        # Filter data for the specific country and parties
        mask = (transformed_data.index.get_level_values("country") == party_group["country"]) & (
            transformed_data.index.get_level_values("party").isin(party_group["parties"])
        )
        party_data = transformed_data[mask]
        if not party_data.empty:
            scatter_plot(
                party_data,
                color=str(party_group["color"]),
                splot=splot,
                size=25,  # Make points larger to be visible
                label=party_group['parties']
            )
            # # Add text labels for each party for better readability
            # for idx, row in party_data.iterrows():
            #     splot.text(row.iloc[0] + 0.1, row.iloc[1], idx[1], fontsize=9)
