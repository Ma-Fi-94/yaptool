import matplotlib  # type: ignore
import matplotlib.pyplot as plt  # type: ignore
import matplotlib.figure  # type: ignore
from matplotlib.patches import Rectangle  # type: ignore

import sys
from typing import Tuple
from typing import List

####################
# Types of layouts #
####################


def singleplot(size=(10, 7)) -> Tuple[matplotlib.figure.Figure, plt.Axes]:
    ''' Make a new 10x7 plot. Size can also be changed. '''
    assert type(size) in (tuple, list)
    assert len(size) == 2
    w, h = size
    assert type(w) in [int, float]
    assert type(h) in [int, float]

    fig, ax = plt.subplots(1, 1, figsize=size)
    return fig, ax


####################
#  Types of plots  #
####################


def lineplot(ax: plt.Axes,
             xs: List[float],
             ys: List[float],
             style: str = "major",
             linewidth: float = 3.0,
             linestyle: str = "-",
             **kwargs):
    assert type(xs) == list
    assert type(ys) == list
    for x in xs:
        assert type(x) in [int, float]

    for y in ys:
        assert type(y) in [int, float]

    pass
    assert len(xs) == len(ys)
    assert type(linewidth) in [int, float]
    assert linewidth > 0
    assert linestyle in ["-", "--", "-.", ":"]

    assert style in ["major", "medium", "minor", "manual"]
    if style == "major":
        linewidth = 3
        linestyle = "-"
    elif style == "medium":
        linewidth = 2
        linestyle = "--"
    elif style == "minor":
        linewidth = 1
        linestyle = ":"

    ax.plot(xs, ys, lw=linewidth, ls=linestyle, **kwargs)


#############################
# Adding elements to a plot #
#############################


def title(ax: plt.Axes,
          title: str,
          fontsize: float = 40,
          pad: float = 20) -> None:
    ''' Add a title to a plot. '''
    assert type(title) == str
    assert type(fontsize) in [int, float]
    assert type(pad) in [int, float]
    assert fontsize > 0
    ax.set_title(title, fontsize=fontsize, pad=pad)


def labels(ax: plt.Axes,
           xlabel: str = None,
           ylabel: str = None,
           fontsize: float = 30,
           pad: float = 15) -> None:
    ''' Add axes labels to a plot. '''
    assert type(fontsize) in [float, int]
    assert fontsize > 0
    assert type(pad) in [float, int]

    if xlabel is not None:
        assert type(xlabel) == str
        ax.set_xlabel(xlabel, fontsize=fontsize, labelpad=pad)

    if ylabel is not None:
        assert type(ylabel) == str
        ax.set_ylabel(ylabel, fontsize=fontsize, labelpad=pad)


def diagonal(ax: plt.Axes,
             colour: str = "black",
             alpha=0.3,
             linestyle="-",
             linewidth=2):
    ''' Add the 45 degrees diagonal to a plot. '''
    assert type(colour) == str
    assert type(alpha) in [float, int]
    assert (alpha >= 0) and (alpha <= 1)
    assert linestyle in ["-", "--", "-.", ":"]
    assert type(linewidth) in [float, int]
    assert linewidth > 0

    minimum = min(ax.get_xlim()[0], ax.get_ylim()[0])
    maximum = max(ax.get_xlim()[1], ax.get_ylim()[1])
    ax.plot([minimum, maximum], [minimum, maximum],
            color=colour,
            linestyle=linestyle,
            linewidth=linewidth,
            alpha=alpha)


def rectangle(ax: plt.Axes,
              x1: float,
              y1: float,
              x2: float,
              y2: float,
              colour: str = "red",
              linewidth: float = 3,
              linestyle: str = "-",
              fill: bool = False,
              **kwargs):
    ''' Add a rectangle to a plot. '''
    assert type(x1) in [int, float]
    assert type(y1) in [int, float]
    assert type(x2) in [int, float]
    assert type(y2) in [int, float]
    assert type(colour) == str
    assert type(linewidth) in [int, float]
    assert linewidth >= 0
    assert linestyle in ["-", "--", "-.", ":"]
    assert type(fill) == bool

    ax.add_patch(
        Rectangle((x1, y1),
                  x2 - x1,
                  y2 - y1,
                  linewidth=linewidth,
                  linestyle=linestyle,
                  edgecolor=colour,
                  facecolor=colour,
                  fill=fill,
                  **kwargs))


def star(ax: plt.Axes,
         x: float,
         y: float,
         colour: str = "red",
         fontsize: float = 50):
    assert type(x) in [int, float]
    assert type(y) in [int, float]
    assert type(fontsize) in [int, float]
    assert type(colour) == str

    ax.annotate("*", (x, y), c=colour, fontsize=fontsize)


#############################
# Change elements of a plot #
#############################


def despine(ax: plt.Axes, which: List[str] = ['top', 'right']):
    ''' Remove spines of ax object. Spines can be specified, default is top and right. '''
    assert type(which) == list
    for spine in which:
        assert spine in ['top', 'right', 'left', 'bottom']
        ax.spines[spine].set_visible(False)


def ticklabelsize(ax: plt.Axes, which: str = "both", size: float = 20):
    ''' Change ticklabelsize of an ax object. '''
    assert type(which) == str
    assert type(size) in [int, float]
    ax.tick_params(which, labelsize=size)


def limits(ax: plt.Axes,
           xlimits: Tuple[float, float] = None,
           ylimits: Tuple[float, float] = None):
    ''' Set axes limits of ax object. '''
    if xlimits is not None:
        assert type(xlimits) in (tuple, list)
        assert len(xlimits) == 2
        lo, hi = xlimits
        assert type(lo) in [int, float]
        assert type(hi) in [int, float]
        ax.set_xlim(xlimits)

    if ylimits is not None:
        assert type(ylimits) in (tuple, list)
        assert len(ylimits) == 2
        lo, hi = ylimits
        assert type(lo) in [int, float]
        assert type(hi) in [int, float]
        ax.set_ylim(ylimits)
