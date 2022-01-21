import matplotlib  # type: ignore
import matplotlib.pyplot as plt  # type: ignore
import matplotlib.figure  # type: ignore
from matplotlib.patches import Rectangle  # type: ignore
from matplotlib import rc  # type: ignore
import seaborn as sns  # type: ignore
from scipy import stats  # type: ignore
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


def _correlation_matrix(list_of_lists: List[List[float]],
                        method: str = "pearson"):
    if type(method) == str:
        if method == "pearson":
            f = lambda a, b: stats.pearsonr(a, b)[0]
        elif method == "spearman":
            f = lambda a, b: stats.spearmanr(a, b)[0]
        elif method == "kendall":
            f = lambda a, b: stats.spearmanr(a, b)[0]
        else:
            raise NotImplementedError
    elif type(method) is types.LambdaType:
        f = method
    else:
        raise NotImplementedError

    results = np.zeros((len(list_of_lists), len(list_of_lists)))
    for i, vec1 in enumerate(list_of_lists):
        for j, vec2 in enumerate(list_of_lists):
            results[i, j] = f(vec1, vec2)
    return results


######################
# General Aesthetics #
######################


def darkmode(foreground="0.85", background="0.15"):
    ''' Switch to darkmode. Foreground and background colours may also be specified explicitly. '''
    _set_fgbg(fg=foreground, bg=background)


def lightmode(foreground="0", background="1.0"):
    ''' Switch to lightmode. Foreground and background colours may also be specified explicitly. '''
    _set_fgbg(fg=foreground, bg=background)


def texon():
    ''' Switch on TeX-rendering of texts. '''
    rc('text', usetex=True)
    params = {'text.latex.preamble': r'\usepackage{amsmath}'}
    plt.rcParams.update(params)


def texoff():
    ''' Switch off TeX-rendering of texts. '''
    rc('text', usetex=False)


####################
# Types of layouts #
####################


def singleplot(size=(10, 7)) -> Tuple[matplotlib.figure.Figure, plt.Axes]:
    ''' Make a new 10x7 plot. Size can also be changed. '''
    try:
        w, h = size
        w = float(w)
        h = float(h)
    except:
        raise AssertionError

    fig, ax = plt.subplots(1, 1, figsize=size)
    return fig, ax


def multiplot(
        nrows: int, ncols: int,
        size_xy: Tuple[float,
                       float],
        wspace: float = None, vspace: float = None) -> Tuple[matplotlib.figure.Figure, plt.Axes]:
    assert type(nrows) == int
    assert type(ncols) == int
    assert nrows > 0
    assert ncols > 0

    try:
        l, h = size_xy
        l = float(l)
        h = float(h)
        if hspace is not None:
            hspace = float(hspace)
        if wspace is not None:
            wspace = float(wspace)
    except:
        raise AssertionError
    assert l > 0
    assert h > 0

    fig, ax = plt.subplots(nrows, ncols, figsize=(h, l))
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
          fontsize: float = 40,
          pad: float = 20) -> None:
    ''' Add a title to a plot. '''
    try:
        title = str(title)
        fontsize = float(fontsize)
        pad = float(pad)
    except:
        raise AssertionError
    assert fontsize > 0
    assert pad > 0
    assert hasattr(ax, 'plot')

    ax.set_title(title, fontsize=fontsize, pad=pad)


def labels(ax: plt.Axes,
           xlabel: str = None,
           ylabel: str = None,
           fontsize: float = 30,
           pad: float = 15) -> None:
    ''' Add axes labels to a plot. '''
    try:
        fontsize = float(fontsize)
        pad = float(pad)
    except:
        raise AssertionError
    assert fontsize > 0
    assert hasattr(ax, 'plot')

    if xlabel is not None:
        try:
            xlabel = str(xlabel)
        except:
            raise AssertionError
        ax.set_xlabel(xlabel, fontsize=fontsize, labelpad=pad)

    if ylabel is not None:
        try:
            ylabel = str(ylabel)
        except:
            raise AssertionError
        ax.set_ylabel(ylabel, fontsize=fontsize, labelpad=pad)


def diagonal(ax: plt.Axes,
             colour: str = "black",
             alpha=0.3,
             linestyle="-",
             linewidth=2):
    ''' Add the 45 degrees diagonal to a plot. '''
    try:
        colour = str(colour)
        alpha = float(alpha)
        linewidth = float(linewidth)
    except:
        raise AssertionError

    assert (alpha >= 0) and (alpha <= 1)
    assert linestyle in ["-", "--", "-.", ":"]
    assert linewidth > 0
    assert hasattr(ax, 'plot')

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
              fill: bool = False):
    ''' Add a rectangle to a plot. '''
    try:
        x1 = float(x1)
        y1 = float(y1)
        x2 = float(x2)
        y2 = float(y2)
        colour = str(colour)
        linewidth = float(linewidth)
    except:
        raise AssertionError
    assert linewidth >= 0
    assert linestyle in ["-", "--", "-.", ":"]
    assert type(fill) == bool
    assert hasattr(ax, 'plot')

    ax.add_patch(
        Rectangle((x1, y1),
                  x2 - x1,
                  y2 - y1,
                  linewidth=linewidth,
                  linestyle=linestyle,
                  edgecolor=colour,
                  facecolor=colour,
                  fill=fill))


def star(ax: plt.Axes,
         x: float,
         y: float,
         colour: str = "red",
         fontsize: float = 50):
    try:
        x = float(x)
        y = float(y)
        fontsize = float(fontsize)
        colour = str(colour)
    except:
        raise AssertionError

    assert fontsize > 0
    assert hasattr(ax, 'plot')

    ax.annotate("*", (x, y), c=colour, fontsize=fontsize)


def lines(ax: plt.Axes,
          which: str,
          pos: List[float],
          colour: str = "black",
          alpha: float = 0.3,
          linestyle: str = "-",
          linewidth: float = 2,
          zorder: float = -100):
    try:
        colour = str(colour)
        alpha = float(alpha)
        linewidth = float(linewidth)
        zorder = int(zorder)
        pos = [float(p) for p in pos]
    except:
        raise AssertionError

    assert which in ["x", "y", "v", "h"]
    assert linestyle in ["-", ":", "--", "-."]
    assert alpha > 0
    assert alpha <= 1
    assert linewidth > 0
    assert len(pos) > 0
    assert hasattr(ax, 'plot')

    if which == "x" or which == "v":
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
    elif which == "y" or which == "h":
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
    try:
        which = list(which)
    except:
        raise AssertionError

    assert hasattr(ax, 'plot')

    for spine in which:
        assert spine in ['top', 'right', 'left', 'bottom']

    for spine in which:
        ax.spines[spine].set_visible(False)


def ticklabelsize(ax: plt.Axes, which: str = "both", size: float = 20):
    ''' Change ticklabelsize of an ax object. '''
    try:
        size = float(size)
    except:
        raise AssertionError

    assert which in ["x", "y", "both"]
    assert hasattr(ax, 'plot')

    ax.tick_params(which, labelsize=size)


def limits(ax: plt.Axes,
           xlimits: Tuple[float, float] = None,
           ylimits: Tuple[float, float] = None):
    assert hasattr(ax, 'plot')
    ''' Set axes limits of ax object. '''
    if xlimits is not None:
        try:
            lo, hi = xlimits
            lo = float(lo)
            hi = float(hi)
        except:
            raise AssertionError

        ax.set_xlim(xlimits)

    if ylimits is not None:
        try:
            lo, hi = ylimits
            lo = float(lo)
            hi = float(hi)
        except:
            raise AssertionError

        ax.set_ylim(ylimits)


############################################################################
def ticks_and_labels(ax: plt.Axes,
                     which: str,
                     ticks: List[float],
                     labels=None):
    try:
        ticks = list(ticks)
        ticks = [float(t) for t in ticks]
    except:
        raise AssertionError

    assert which in ["x", "y", "xy", "yx"]
    assert hasattr(ax, 'plot')

    if labels is None:
        labels = list(map(lambda x: str(x), ticks))
    else:
        try:
            labels = list(labels)
        except:
            raise AssertionError

        assert len(ticks) == len(labels)

    if which == "x" or which == "xy" or which == "yx":
        ax.set_xticks(ticks)
        ax.set_xticklabels(labels)
    if which == "y" or which == "xy" or which == "yx":
        ax.set_yticks(ticks)
        ax.set_yticklabels(labels)


def rotate_ticklabels(ax: plt.Axes, which: str, rotation: float):
    assert which in ["x", "y", "xy", "yx", "both"]
    assert hasattr(ax, 'plot')
    try:
        rotation = float(rotation)
    except:
        raise AssertionError

    if which == "x" or which == "xy" or which == "yx" or which == "both":
        ax.set_xticklabels(ax.get_xticklabels(), rotation=rotation)
    if which == "y" or which == "xy" or which == "yx" or which == "both":
        ax.set_yticklabels(ax.get_yticklabels(), rotation=rotation)


def align_ticklabels(ax: plt.Axes, which: str, horizontal: str, vertical: str):
    assert which in ["x", "y"]
    assert hasattr(ax, 'plot')

    if which == "x":
        if horizontal is not None:
            assert horizontal in ['center', 'right', 'left']
            ax.set_xticklabels(ax.get_xticklabels(),
                               horizontalalignment=horizontal)
        if vertical is not None:
            assert vertical in ['center', 'top', 'bottom', 'baseline']
            ax.set_xticklabels(ax.get_xticklabels(),
                               verticalalignment=vertical)

    if which == "y":
        if horizontal is not None:
            assert horizontal in ['center', 'right', 'left']
            ax.set_yticklabels(ax.get_yticklabels(),
                               horizontalalignment=horizontal)
        if vertical is not None:
            assert vertical in ['center', 'top', 'bottom', 'baseline']
            ax.set_yticklabels(ax.get_yticklabels(),
                               verticalalignment=vertical)


#########
# Plots #
#########


def similarity_heatmap(ax: plt.Axes,
                       list_of_lists: List[List[float]],
                       method: str = "jaccard"):
    assert hasattr(ax, 'plot')
    sns.heatmap(_similarity_matrix(list_of_lists, method))


def correlations_heatmap(ax: plt.Axes,
                         list_of_lists: List[List[float]],
                         method: str = "pearson"):
    assert hasattr(ax, 'plot')
    sns.heatmap(_correlation_matrix(list_of_lists, method))


def masked_heatmap(ax: plt.Axes, data: np.ndarray, mask: str, **kwargs):
    try:
        data = np.array(data)
    except:
        raise AssertionError

    assert mask in ["lower", "upper", "lowerdiag", "upperdiag"]
    assert hasattr(ax, 'plot')

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


def save_png(filename: str, dpi: float = 300):
    ''' Save current figure as png file. DPI can be specified. '''
    try:
        filename = str(filename)
        dpi = float(dpi)
    except:
        raise AssertionError

    assert filename != ""
    assert dpi > 0
    plt.savefig(filename, dpi=dpi, bbox_inches="tight",
                format="png")  # pragma: no cover


def save_svg(filename: str):
    ''' Save current figure as svg file. '''
    try:
        filename = str(filename)
    except:
        raise AssertionError

    assert filename != ""
    plt.savefig(filename, bbox_inches="tight",
                format="svg")  # pragma: no cover


def save_pdf(filename: str):
    ''' Save current figure as pdf file. '''
    try:
        filename = str(filename)
    except:
        raise AssertionError

    assert filename != ""

    plt.savefig(filename, bbox_inches="tight",
                format="pdf")  # pragma: no cover


######################
# Default parameters #
######################


def heatmap_cbar_kws():
    return {'fraction': 0.1, 'shrink': 0.4, 'aspect': 7, 'pad': 0.05}


def heatmap_annot_kws():
    return {'fontsize': 20}


##########################
# Some ideas, TBD nicely #
##########################


def majorline(ax, x, y, linewidth=3, linestyle="-", **kwargs):
    ax.plot(x, y, lw=linewidth, ls=linestyle, **kwargs)


def midiline(ax, x, y, linewidth=2, linestyle="--", **kwargs):
    ax.plot(x, y, lw=linewidth, ls=linestyle, **kwargs)


def minorline(ax, x, y, linewidth=1, linestyle=":", **kwargs):
    ax.plot(x, y, lw=linewidth, ls=linestyle, **kwargs)


def legend(ax, loc="best", fontsize=25, frame=False, **kwargs):
    ''' Add a legend to a plot. '''
    l = ax.legend(loc=loc, fontsize=fontsize, frameon=frame, **kwargs)
    try:
        for lh in l.legendHandles:
            lh._legmarker.set_alpha(1)
    except:
        pass
    try:
        for lh in l.legendHandles:
            lh.set_alpha(1)
    except:
        pass


def oligoscatter(ax, x, y, marker="o", alpha=1, **kwargs):
    ax.scatter(x, y, marker=marker, alpha=alpha, **kwargs)


def oligoscatter_errorbar(ax,
                          x,
                          y,
                          xerr=None,
                          yerr=None,
                          marker="o",
                          alpha=1,
                          **kwargs):
    ax.errorbar(x,
                y,
                xerr=xerr,
                yerr=yerr,
                marker=marker,
                alpha=alpha,
                **kwargs)


def polyscatter(ax, x, y, marker=".", alpha=0.5, **kwargs):
    ax.scatter(x, y, marker=marker, alpha=alpha, **kwargs)


def polyscatter_errorbar(ax,
                         x,
                         y,
                         xerr=None,
                         yerr=None,
                         marker="o",
                         alpha=1,
                         **kwargs):
    ax.errorbar(x,
                y,
                xerr=xerr,
                yerr=yerr,
                marker=marker,
                alpha=alpha,
                **kwargs)
