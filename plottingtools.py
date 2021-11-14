import matplotlib  # type: ignore
import matplotlib.pyplot as plt  # type: ignore
import matplotlib.figure  # type: ignore
from matplotlib.patches import Rectangle  # type: ignore
import seaborn as sns  # type: ignore
import numpy as np
import sys
import types

from typing import Tuple
from typing import List

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


def _similarity_matrix(list_of_lists: List[List[float]],
                       method: str = "jaccard"):
    if type(method) == str:
        if method == "jaccard":
            f = lambda s1, s2: len(set.intersection(s1, s2)) / len(
                set.union(s1, s2))
        else:
            raise NotImplementedError
    elif type(method) is types.LambdaType:
        f = method
    else:
        raise NotImplementedError

    results = np.zeros((len(list_of_lists), len(list_of_lists)))

    list_of_sets = list(map(lambda l: set(l), list_of_lists))

    # Some similarity functions are not symmetric
    # Hence we iterate over all n x n combinations
    for i, set1 in enumerate(list_of_sets):
        for j, set2 in enumerate(list_of_sets):
            results[i, j] = f(set1, set2)
    return results


#################
# Colour Themes #
#################


def darkmode(foreground="0.85", background="0.15"):
    ''' Switch to darkmode. Foreground and background colours may also be specified explicitly. '''
    _set_fgbg(fg=foreground, bg=background)


def lightmode(foreground="0", background="1.0"):
    ''' Switch to lightmode. Foreground and background colours may also be specified explicitly. '''
    _set_fgbg(fg=foreground, bg=background)


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


def multiplot(
        nrows: int, ncols: int,
        size_xy: Tuple[float,
                       float]) -> Tuple[matplotlib.figure.Figure, plt.Axes]:
    assert type(nrows) == int
    assert type(ncols) == int
    assert nrows > 0
    assert ncols > 0
    l, h = size_xy
    assert type(l) in [float, int]
    assert type(h) in [float, int]
    assert l > 0
    assert h > 0

    fig, ax = plt.subplots(nrows, ncols, figsize=(h, l))
    return fig, ax


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


def lines(ax: plt.Axes,
          which: str,
          pos: List[float],
          colour: str = "black",
          alpha: float = 0.3,
          linestyle: str = "-",
          linewidth: float = 2,
          zorder: float = -100):
    assert type(which) == str
    assert which in ["x", "y"]

    assert type(pos) == list
    assert len(pos) > 0
    for x in pos:
        assert type(x) in [int, float]

    assert type(colour) == str

    assert type(alpha) in [int, float]
    assert alpha > 0
    assert alpha <= 1

    assert type(linestyle) == str
    assert linestyle in ["-", ":", "--", "-."]

    assert type(linewidth) in [int, float]
    assert linewidth > 0

    assert type(zorder) in [int, float]

    if which == "x":
        ymin, ymax = ax.get_ylim()
        for x in pos:
            ax.vlines([x],
                      ymin,
                      ymax,
                      color=colour,
                      alpha=alpha,
                      linestyle=linestyle,
                      linewidth=linewidth,
                      zorder=zorder)
    elif which == "y":
        xmin, xmax = ax.get_xlim()
        for y in pos:
            ax.hlines([y],
                      xmin,
                      xmax,
                      color=colour,
                      alpha=alpha,
                      linestyle=linestyle,
                      linewidth=linewidth,
                      zorder=zorder)


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


def ticks_and_labels(ax: plt.Axes,
                     which: str,
                     ticks: List[float],
                     labels=None):
    assert which in ["x", "y", "xy", "yx"]
    assert type(ticks) == list
    for tick in ticks:
        assert type(tick) in [float, int]

    if labels is None:
        labels = list(map(lambda x: str(x), ticks))
    else:
        assert type(labels) == list
        assert len(ticks) == len(labels)

    if which == "x" or which == "xy" or which == "yx":
        ax.set_xticks(ticks)
        ax.set_xticklabels(labels)
    if which == "y" or which == "xy" or which == "yx":
        ax.set_yticks(ticks)
        ax.set_yticklabels(labels)


def rotate_ticklabels(ax: plt.Axes, which: str, rotation: float):
    assert type(which) == str
    assert which in ["x", "y", "xy", "yx", "both"]
    assert type(rotation) in [float, int]

    if which == "x" or which == "xy" or which == "yx" or which == "both":
        ax.set_xticklabels(ax.get_xticklabels(), rotation=rotation)
    if which == "y" or which == "xy" or which == "yx" or which == "both":
        ax.set_yticklabels(ax.get_yticklabels(), rotation=rotation)


def align_ticklabels(ax: plt.Axes, which: str, horizontal: str, vertical: str):
    assert type(which) == str
    assert which in ["x", "y"]

    if which == "x":
        if horizontal is not None:
            assert type(horizontal) == str
            assert horizontal in ['center', 'right', 'left']
            ax.set_xticklabels(ax.get_xticklabels(),
                               horizontalalignment=horizontal)
        if vertical is not None:
            assert type(vertical) == str
            assert vertical in ['center', 'top', 'bottom', 'baseline']
            ax.set_xticklabels(ax.get_xticklabels(),
                               verticalalignment=vertical)

    if which == "y":
        if horizontal is not None:
            assert type(horizontal) == str
            assert horizontal in ['center', 'right', 'left']
            ax.set_yticklabels(ax.get_yticklabels(),
                               horizontalalignment=horizontal)
        if vertical is not None:
            assert type(vertical) == str
            assert vertical in ['center', 'top', 'bottom', 'baseline']
            ax.set_yticklabels(ax.get_yticklabels(),
                               verticalalignment=vertical)


#########
# Plots #
#########


def similarity_heatmap(ax: plt.Axes,
                       list_of_lists: List[List[float]],
                       method: str = "jaccard"):
    sns.heatmap(_similarity_matrix(list_of_lists, method))


def masked_heatmap(ax: plt.Axes, data: np.ndarray, mask: str, **kwargs):
    assert type(data) == np.ndarray

    assert type(mask) == str
    assert mask in ["lower", "upper", "lowerdiag", "upperdiag"]

    if mask == "upperdiag":
        mask_array = np.triu(data, k=0)
    elif mask == "upper":
        mask_array = np.triu(data, k=1)
    elif mask == "lowerdiag":
        mask_array = np.tril(data, k=0)
    elif mask == "lower":
        mask_array = np.tril(data, k=-1)

    sns.heatmap(data, ax=ax, mask=mask_array)


##################
# Export figures #
##################


def save_png(filename: str, dpi: int = 300):
    ''' Save current figure as png file. DPI can be specified. '''
    assert type(filename) == str
    assert filename != ""
    assert type(dpi) in [int, float]
    assert dpi > 0
    plt.savefig(filename, dpi=dpi, bbox_inches="tight", format="png")


def save_svg(filename: str):
    ''' Save current figure as svg file. '''
    assert type(filename) == str
    assert filename != ""
    plt.savefig(filename, bbox_inches="tight", format="svg")


######################
# Default parameters #
######################


def heatmap_cbar_kws():
    return {'fraction': 0.1, 'shrink': 0.4, 'aspect': 7, 'pad': 0.05}


def heatmap_annot_kws():
    return {'fontsize': 20}
