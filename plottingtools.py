"""A collection of handy functions to avoid boilerplate code while using matplotlib."""

__version__ = "0.1"

from typing import List, Optional, Tuple, Union

import matplotlib  # type: ignore
import matplotlib.figure  # type: ignore
import matplotlib.pyplot as plt  # type: ignore
from matplotlib import rc  # type: ignore
from matplotlib.patches import Rectangle  # type: ignore

####################
# Internal helpers #
####################


def _set_fgbg(fg: str, bg: str):
    ''' Internal helper to change fore- and background colours '''
    plt.rcParams.update({
        "lines.color": fg,
        "patch.edgecolor": fg,
        "text.color": fg,
        "axes.facecolor": bg,
        "axes.edgecolor": fg,
        "axes.labelcolor": fg,
        "xtick.color": fg,
        "ytick.color": fg,
        "grid.color": fg,
        "figure.facecolor": bg,
        "figure.edgecolor": bg,
        "savefig.facecolor": bg,
        "savefig.edgecolor": bg
    })


######################
# General Aesthetics #
######################


def darkmode(foreground: str = "0.85", background: str = "0.15") -> None:
    """Switches to dark mode.
    Foreground and background colours may also be specified explicitly.

    Args:
        foreground:
            An optional string, specifying the foreground colour,
            following matplotlib's colour syntax. Defaults to "0.85", i.e. light grey.
        background:
            An optional string, specifying the background colour,
            following matplotlib's colour syntax. Defaults to "0.15", i.e. dark grey.

    Returns:
        None
    """
    _set_fgbg(fg=foreground, bg=background)


def lightmode(foreground: str = "0", background: str = "1.0") -> None:
    """Switches to light mode.
    Foreground and background colours may also be specified explicitly.

    Args:
        foreground:
            An optional string, specifying the foreground colour,
            following matplotlib's colour syntax. Defaults to "0", i.e. black.
        background:
            An optional string, specifying the background colour,
            following matplotlib's colour syntax. Defaults to "1.0", i.e. white.

    Returns:
        None
    """
    _set_fgbg(fg=foreground, bg=background)


def texon() -> None:
    """Switches on TeX-rendering of texts.

    Args:
        None

    Returns:
        None
    """
    rc('text', usetex=True)
    params = {'text.latex.preamble': r'\usepackage{amsmath}'}
    plt.rcParams.update(params)


def texoff() -> None:
    """Switches off TeX-rendering of texts.

    Args:
        None

    Returns:
        None
    """
    rc('text', usetex=False)


####################
# Types of layouts #
####################


def singleplot(size: Tuple[float, float] = (
    10, 7)) -> Tuple[matplotlib.figure.Figure, plt.Axes]:
    """Generates a new single-plot figure.
    The figure size may be defined explicitly.

    Args:
        size:
            An optional tuple of two floats, containing
            the desired figure width and heigth in inches.
            Defaults to 10x7 inches.

    Returns:
        fig:
            A matplotlib.figure.Figure instance
        ax:
            A pyplot.Axes instance
    """

    fig, ax = plt.subplots(1, 1, figsize=size)
    return fig, ax


def multiplot(
    nrows: int,
    ncols: int,
    size_xy: Tuple[float, float],
    wspace: Optional[float] = None,
    hspace: Optional[float] = None
) -> Tuple[matplotlib.figure.Figure, plt.Axes]:
    """Generates a new figure consisting of nrows rows
    and ncols columns of plots with overall figure size size_xy.
    Horizontal and vertical distance between plots may be defined explicitly.

    Args:
        size:
            An tuple of two floats, containing the desired
            figure width and heigth in inches.
        wspace:
            An optional float, specifying the horizontal
            distance between columns. Defaults to zero.
        hspace:
            An optional float, specifying the vertical
            distance between rows. Defaults to zero.

    Returns:
        fig:
            A matplotlib.figure.Figure instance
        ax:
            An array of pyplot.Axes instances
    """

    fig, ax = plt.subplots(nrows, ncols, figsize=size_xy)
    if hspace is not None:
        plt.subplots_adjust(hspace=hspace)
    if wspace is not None:
        plt.subplots_adjust(wspace=wspace)
    return fig, ax


#############################
# Adding elements to a plot #
#############################


def title(ax: plt.Axes,
          title: str,
          fontsize: float = 30,
          pad: float = 20) -> None:
    """Adds a title to an existing plot.

    Args:
        ax:
            A pyplot.Axes instance
        title:
            A string containing the title to add.
        fontsize:
            An optional float, specifying the font
            size of the title. Defaults to 30.
        pad:
            An optional float, specifying the padding
            between title and figure. Defaults to 20.

    Returns:
        None
    """

    if not hasattr(ax, 'plot'):
        raise ValueError("Pass a valid plot in parameter ax.")

    ax.set_title(title, fontsize=fontsize, pad=pad)


def labels(ax: plt.Axes,
           xlabel: Optional[str] = None,
           ylabel: Optional[str] = None,
           fontsize: float = 30,
           pad: float = 15) -> None:
    """Adds axes labels to an existing plot.

    Args:
        ax:
            A pyplot.Axes instance
        xlabel:
            An optional string containing the label to be
            added to the x-axis of the plot.
        ylabel:
            An optional string containing the label to be
            added to the y-axis of the plot.
        fontsize:
            An optional float, specifying the font size of
            the labels. Defaults to 30.
        pad:
            An optional float, specifying the padding between
            labels and figure. Defaults to 15.

    Returns:
        None
    """

    if not hasattr(ax, 'plot'):
        raise ValueError("Pass a valid plot in parameter ax.")

    if xlabel is not None:
        ax.set_xlabel(xlabel, fontsize=fontsize, labelpad=pad)

    if ylabel is not None:
        ax.set_ylabel(ylabel, fontsize=fontsize, labelpad=pad)


def diagonal(ax: plt.Axes,
             colour: str = "black",
             alpha: float = 0.3,
             linestyle: str = "-",
             linewidth: float = 2) -> None:
    """Adds the 45 degrees diagonal to an existing plot.

    Args:
        ax:
            A pyplot.Axes instance
        colour:
            An optional string containing the colour of the diagonal
            to be added. Defaults to "black".
        alpha:
            An optional float containing the alpha (opacity) of the
            diagonal to be added. Defaults to 0.3.
        linestyle:
            An optional string, specifying the line style of the
            diagonal to be added, Defaults to "-", i.e. a continuous line.
        linewidth:
            An optional float, specifying the width (in px) of the
            diagonal to be added. Defaults to 2.

    Returns:
        None
    """

    if not hasattr(ax, 'plot'):
        raise ValueError("Pass a valid plot in parameter ax.")

    minimum = min(ax.get_xlim()[0], ax.get_ylim()[0])
    maximum = max(ax.get_xlim()[1], ax.get_ylim()[1])
    ax.plot([minimum, maximum], [minimum, maximum],
            color=colour,
            linestyle=linestyle,
            linewidth=linewidth,
            alpha=alpha)


def rectangle(ax: plt.Axes, x1: float, y1: float, x2: float, y2: float,
              **kwargs) -> None:
    """Convenience function for addig a rectangle to an existing plot
    without having to manually call ax.add_patch(). Takes x and y
    coordinates of two points as arguments, instead of the x and y
    coordinate of one point and the rectagle width and heigth,
    like add_patch() would.

    Args:
        ax:
            A pyplot.Axes instance
        x1:
            A float, specifying the x coordinate of the first point.
        y1:
            A float, specifying the y coordinate of the first point.
        x2:
            A float, specifying the x coordinate of the second point.
        y2:
            A float, specifying the y coordinate of the second point.
        **kwargs:
            Named arguments such as color, fill, linewidth, linestyle.
            Passed to ax.add_patch().

    Returns:
        None
    """
    try:
        x1 = float(x1)
        y1 = float(y1)
        x2 = float(x2)
        y2 = float(y2)
    except Exception as ex:
        raise ValueError("Pass numbers in x1, y1, x2, y2.") from ex

    if not hasattr(ax, 'plot'):
        raise ValueError("Pass a valid plot in parameter ax.")

    ax.add_patch(Rectangle((x1, y1), x2 - x1, y2 - y1, **kwargs))


def legend(ax: plt.Axes,
           loc: Union["str", int] = "best",
           fontsize: float = 30,
           frame: bool = False,
           **kwargs) -> None:
    """Adds a legend to an existing plot.

    Args:
        ax:
            A pyplot.Axes instance
        loc:
            A string, specifying the legend position,
            following matplotlib syntax. Defaults to "best".
        fontsize:
            A float, specifying the font size. Defaults to 30.
        frame:
            A bool, specifying whether to draw a frame around the legend.
            Defaults to false, i.e. no.
        **kwargs:
            Named arguments such as color, fill, linewidth, linestyle.
            Passed to ax.legend().

    Returns:
        None
    """

    if not hasattr(ax, 'plot'):
        raise ValueError("Pass a valid plot in parameter ax.")

    l = ax.legend(loc=loc, fontsize=fontsize, frameon=frame, **kwargs)

    # Automatically try to set correct alpha for legend symbols
    try:
        for lh in l.legendHandles:
            lh._legmarker.set_alpha(1)
    except Exception:
        pass

    # Automatically try to set correct alpha for legend symbols another way
    try:
        for lh in l.legendHandles:
            lh.set_alpha(1)
    except Exception:
        pass


#############################
# Change elements of a plot #
#############################


def despine(ax: plt.Axes, which: List[str] = ['top', 'right']) -> None:
    """Remove spines of an existing plot.
    Spines can be specified, default is top and right.

    Args:
        ax:
            A pyplot.Axes instance
        which:
            A list of strings, specifying which spines to remove.
            Defaults to ["top", "right"].
            Also possible are "bottom" and "left".

    Returns:
        None
    """

    if not hasattr(ax, 'plot'):
        raise ValueError("Pass a valid plot in parameter ax.")

    for spine in which:
        ax.spines[spine].set_visible(False)


def respine(ax: plt.Axes, which: List[str] = ['top', 'right']) -> None:
    """Adds spines to an existing plot.
    Spines can be specified, default is top and right.

    Args:
        ax:
            A pyplot.Axes instance
        which:
            A list of strings, specifying which spines to add.
            Defaults to ["top", "right"].
            Also possible are "bottom" and "left".

    Returns:
        None
    """

    if not hasattr(ax, 'plot'):
        raise ValueError("Pass a valid plot in parameter ax.")

    for spine in which:
        ax.spines[spine].set_visible(True)


def ticklabelsize(ax: plt.Axes, which: str = "both", size: float = 30) -> None:
    """Changes ticklabelsize of an existing plot.

    Args:
        ax:
            A pyplot.Axes instance
        which:
            A string, specifying the axes for which tick label size is changed.
            Possible are "x", "y", and "both". Defaults to "both".
        size:
            A float, specifying the desired tick label size. Defaults to 30.

    Returns:
        None
    """

    if not hasattr(ax, 'plot'):
        raise ValueError("Pass a valid plot in parameter ax.")

    ax.tick_params(which, labelsize=size)


def limits(ax: plt.Axes,
           xlimits: Optional[Tuple[float, float]] = None,
           ylimits: Optional[Tuple[float, float]] = None) -> None:
    """Sets ax limits of an existing plot.

    Args:
        ax:
            A pyplot.Axes instance
        xlimits:
            An optional tuple of two floats,
            containing the desired limits of the x-axis. Defaults to None.
        ylimits:
            An optional tuple of two floats,
            containing the desired limits of the x-axis. Defaults to None.

    Returns:
        None
    """

    if not hasattr(ax, 'plot'):
        raise ValueError("Pass a valid plot in parameter ax.")

    if xlimits is not None:
        ax.set_xlim(xlimits)

    if ylimits is not None:
        ax.set_ylim(ylimits)


def ticks_and_labels(ax: plt.Axes,
                     which: str,
                     ticks: List[float],
                     labels: Optional[List[str]] = None) -> None:
    """Sets ticks and corresponding labels of one or both axes of an existing plot.

    Args:
        ax:
            A pyplot.Axes instance
        which:
            A string, specifying the axis.
            Possible values are "x", "y", "xy", "yx", "both".
        ticks:
            A list of floats, containing the desired tick positions.
        labels:
            An optional list of strings, containing the desired
            axis labels corresponding to the specified tick positions.
            Defaults to None. If no list is provided, tick labels will
            be set to the numerical values of the provided ticks positions.

    Returns:
        None
    """

    if not which in ["x", "y", "xy", "yx", "both"]:
        raise ValueError(
            'Parameter which must be one of "x", "y", "xy", "yx", "both".')

    if not hasattr(ax, 'plot'):
        raise ValueError("Pass a valid plot in parameter ax.")

    if labels is None:
        labels = list(map(lambda x: str(x), ticks))

    if which in ["x", "xy", "yx", "both"]:
        ax.set_xticks(ticks)
        ax.set_xticklabels(labels)

    if which in ["y", "xy", "yx", "both"]:
        ax.set_yticks(ticks)
        ax.set_yticklabels(labels)


def rotate_ticklabels(ax: plt.Axes, which: str, rotation: float) -> None:
    """Rotates tick labels of one or both axes of an existing plot.

    Args:
        ax:
            A pyplot.Axes instance
        which:
            A string, specifying the axis. Possible values are "x", "y", "xy", "yx", "both".
        rotation:
            A float, containing the tick label angle.

    Returns:
        None
    """

    if not which in ["x", "y", "xy", "yx", "both"]:
        raise ValueError(
            'Parameter which must be one of "x", "y", "xy", "yx", "both".')

    if not hasattr(ax, 'plot'):
        raise ValueError("Pass a valid plot in parameter ax.")

    if which in ["x", "xy", "yx", "both"]:
        ax.set_xticklabels(ax.get_xticklabels(), rotation=rotation)

    if which in ["y", "xy", "yx", "both"]:
        ax.set_yticklabels(ax.get_yticklabels(), rotation=rotation)


def align_ticklabels(ax: plt.Axes,
                     which: str,
                     horizontal: Optional[str] = None,
                     vertical: Optional[str] = None) -> None:
    """Aligns tick labels of one axis of an existing plot.
    Both horizontal and vertical alignment may be specified.

    Args:
        ax:
            A pyplot.Axes instance
        which:
            A string, specifying the axis. Possible values are "x", "y".
        horizontal:
            An optional string, containing the desired horizontal
            tick label alignment. Possible values are "center",
            "right", "left". Defaults to None, i.e. no change.
        vertical:
            An optional string, containing the desired vertical
            tick label alignment. Possible values are "center",
            "top", "bottom", "baseline". Defaults to None, i.e. no change.

    Returns:
        None
    """

    if not which in ["x", "y"]:
        raise ValueError('Parameter which must be one of "x", "y".')

    if not hasattr(ax, 'plot'):
        raise ValueError("Pass a valid plot in parameter ax.")

    if which == "x":
        if horizontal is not None:
            ax.set_xticklabels(ax.get_xticklabels(),
                               horizontalalignment=horizontal)
        if vertical is not None:
            ax.set_xticklabels(ax.get_xticklabels(),
                               verticalalignment=vertical)

    if which == "y":
        if horizontal is not None:
            ax.set_yticklabels(ax.get_yticklabels(),
                               horizontalalignment=horizontal)
        if vertical is not None:
            ax.set_yticklabels(ax.get_yticklabels(),
                               verticalalignment=vertical)


##################
# Export figures #
##################


def save_png(filename: str, dpi: float = 300) -> None:
    """Exports the currently active figure as PNG file. DPI may be specified.

    Args:
        filename:
            A string, containing the path and filename for exporting.
        dpi:
            An optional float, specifying the desired DPI. Defaults to 300.

    Returns:
        None
    """
    plt.savefig(filename, dpi=dpi, bbox_inches="tight",
                format="png")  # pragma: no cover


def save_svg(filename: str) -> None:
    """Exports the currently active figure as SVG file.

    Args:
        filename:
            A string, containing the path and filename for exporting.

    Returns:
        None
    """

    plt.savefig(filename, bbox_inches="tight",
                format="svg")  # pragma: no cover


def save_pdf(filename: str) -> None:
    """Exports the currently active figure as PDF file.

    Args:
        filename:
            A string, containing the path and filename for exporting.

    Returns:
        None
    """

    plt.savefig(filename, bbox_inches="tight",
                format="pdf")  # pragma: no cover


##########################
# Some ideas, TBD nicely #
##########################


def majorline(ax,
              x,
              y,
              linewidth=3,
              linestyle="-",
              **kwargs):  # pragma: no cover
    ax.plot(x, y, lw=linewidth, ls=linestyle, **kwargs)


def minorline(ax,
              x,
              y,
              linewidth=1,
              linestyle=":",
              **kwargs):  # pragma: no cover
    ax.plot(x, y, lw=linewidth, ls=linestyle, **kwargs)


def oligoscatter(ax, x, y, marker="o", alpha=1, **kwargs):  # pragma: no cover
    ax.scatter(x, y, marker=marker, alpha=alpha, **kwargs)


def polyscatter(ax, x, y, marker=".", alpha=0.5, **kwargs):  # pragma: no cover
    ax.scatter(x, y, marker=marker, alpha=alpha, **kwargs)
