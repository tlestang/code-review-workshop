"""Module providing utility function to generate an highly-customisable Bar Plot from data gathered from pandas DataFrame."""

import os
import matplotlib.pyplot as plt
import pandas as pd

from typing import Union
from itertools import filterfalse
from pathlib import Path
from textwrap import wrap

# Chart Data Folder
CHART_FOLDER = Path("/home/ggk765/Analysis/Charts")
if not os.path.exists(CHART_FOLDER):
    os.makedirs(CHART_FOLDER, exist_ok=True)

default_color_map = plt.get_cmap("Set2")


def bar_plot(
    df: pd.DataFrame,
    columns: list[str],
    title: str,
    filename: Union[Path, str] = None,
    unstack_ord: tuple[int] = None,
    selection: pd.DataFrame = None,
    aggregate: str = "value_counts",
    sorted: str = "index",
    legend: bool = True,
    legend_loc: tuple[int, int] = None,
    legend_col: int = None,
    axis_label: str = None,
    value_lim: int = None,
    wrapping: int = 20,
    figsize: tuple[int] = (12, 6),
    width: float = 0.5,
    alpha: float = 0.5,
    horizontal: bool = False,
    colors: list[tuple[float]] = default_color_map.colors,
) -> None:
    """
    Utility function to visualise data (descriptive) statistics as a bar plot.

    The bar plot is rather customisable in both data selection, and figure attributes
    (e.g. figsize, horizontal or vertical bars, legend).
    Option to save the bar plot in a PDF file, instead of just visualising it.

    Parameters
    ----------
    df : pd.DataFrame
        Data Frame containing the reference data
    columns : list[str]
        List of columns in the Data Frame to select from the original data frame.
        If None or empty list will be provided, all data frame columns will be considered instead, although quite unlikely.
        Similarly, if any column name will not be found in the dataframe, an exception will be raised.
    title : str
        Title of the plot
    filename : Union[Path, str], optional
        Name of the PDF file to save containing the whole barplot figure.
    unstack_ord : tuple[int], optional
        Tuple of indices of the corresponding index to repeatedly unstack from the resulting statistics-dataframe, if any.
        By default is None, meaning no `unstack` operation will be applied nor tempted to the resulting dataframe.
    selection : pd.DataFrame, optional
        Filter to apply on data prior generating the plot, by default None.
        This filter should be specified in any form compliant to pandas data selection mechanism.
    aggregate : str, optional
        Name of the pandas function to apply to gather the statistics from the data, by default "value_counts"
    legend : bool, optional
        Optional parameter to control whether a legend should be added to the barplot. If True (default), a legend will be added
        only if more than one column (series) of data was selected. No legend will be added otherwise. Conversely, if this parameter
        is passed to as False, no legend will be added, regardless.
    legend_loc: tuple[int, int], optional
        If legend=True, this parameter will determine the location of the legend. Ignored otherwise. If not provided, legend will be shown according to the type of bar plot (i.e. horizontal=True|False)
    legend_col: int, optional
        if legend=True, this parameter will control the number of columns
        of the chart legend. Ignored otherwise.
        Default values are 3 for bar plot, and 1 for barh.
    axis_label: str, optional
        If provided, this parameter will be used as label for the x-axis (y-axis if horizontal=True). Otherwise the
        name of the corresponding column in the dataframe will be used instead (default).
    value_lim: int, optional
        If provided, this value will set the limit of the x (or y) axis depending on whether the
        bar plot is vertical or not.
    wrapping: int, optional
        Parameter to control spacing of ticks in the barplot, 20 by default.
    figsize : tuple[int], optional
        Size of the generated Matplotlib figure, by default (12, 6)
    width : float, optional
        Width of the bars in the bar plot, by default 0.5
    alpha : float, optional
        Alpha value of colours of each series, by default 0.5
    horizontal : bool, optional
        Flag controlling whether bar plot should be horizontal or vertical. By default False, which will generate a bar plot.
    colors : list[tuple[float]], optional
        List of colours to apply to each series, by default the "Dark2" Matplotlib Colormap will be used.
        Please note that the number of provided colours must be greater or equal to the number of data series in the plot.

    Raises
    ------
    ValueError
        If coloumns or groupby_cols specified are not found in the reference dataframe
    ValueError
        If the value of sorted parameter is not one of "index", "value", None.
    """
    if columns is None or not len(columns):
        columns = df.columns

    if legend_loc is None:
        if not horizontal:
            legend_loc = (0, 1.1)
        else:
            legend_loc = (1, 0)

    if legend_col is None:
        if not horizontal:
            legend_col = 3
        else:
            legend_col = 1

    if any([col not in df.columns for col in columns]):
        not_found = list(filterfalse(lambda c: c in df.columns, columns))
        raise ValueError(
            f"Invalid specified columns. Column{'s' if len(not_found) > 1 else ''} {not_found} cannot be found in input dataframe."
        )

    if not aggregate:
        aggregate = "value_counts"

    if not sorted in ("index", "values", None):
        raise ValueError(
            "Invalid value for sorted parameter. Accepted values are 'index', 'values', or 'None'"
        )

    if len(columns) == 1:
        columns = columns[0]
    else:
        columns = list(columns)

    if selection is not None:
        df_chart = df[selection][columns]
    else:
        df_chart = df[columns]

    agg = getattr(df_chart, aggregate)
    df_chart = agg()

    if sorted is not None:
        if sorted == "index":
            df_chart = df_chart.sort_index()
        else:
            df_chart = df_chart.sort_values(ascending=False)

    if isinstance(columns, list) and unstack_ord is not None:
        for idx in unstack_ord:
            df_chart = df_chart.unstack(idx)

    if not horizontal:
        ax = df_chart.plot.bar(
            figsize=figsize,
            width=width,
            color=colors,
            alpha=alpha,
            title=title,
            fontsize="x-large",
        )
        xticks_labels = ["\n".join(wrap(l, wrapping)) for l in df_chart.index.values]
        ax.set_xticks(range(len(xticks_labels)), labels=xticks_labels)
        if axis_label:
            ax.set_xlabel(axis_label, fontsize="x-large")
    else:
        ax = df_chart.plot.barh(
            figsize=figsize,
            width=width,
            color=colors,
            alpha=alpha,
            title=title,
            fontsize="x-large",
        )
        yticks_labels = ["\n".join(wrap(l, wrapping)) for l in df_chart.index.values]
        ax.set_yticks(range(len(yticks_labels)), labels=yticks_labels)
        if axis_label:
            ax.set_ylabel(axis_label, fontsize="x-large")

    if legend and isinstance(columns, list):
        # adding legend only if more than one column is being selected
        plt.legend(ncol=legend_col, loc=legend_loc)
    elif not legend:
        ax.legend().set_visible(False)

    for container in ax.containers:
        labels = [
            str(int(value)) if value > 0 else "" for value in container.datavalues
        ]
        ax.bar_label(container, labels=labels, fontsize="x-large")

    if value_lim is not None:
        if horizontal:
            ax.set_xlim(0, abs(value_lim))
        else:
            ax.set_ylim(0, abs(value_lim))

    if filename:
        chart_filepath = CHART_FOLDER / filename
        if filename and not filename.endswith(".pdf"):
            filename += ".pdf"
        plt.savefig(
            chart_filepath, dpi=1200, format="pdf", pad_inches=0.5, bbox_inches="tight"
        )
    else:
        plt.show()
