import matplotlib  # type: ignore
import matplotlib.pyplot as plt  # type: ignore
import matplotlib.figure  # type: ignore

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
    ax.set_title(title, fontsize=fontsize, pad=pad)


def labels(ax: plt.Axes,
           xlabel: str = None,
           ylabel: str = None,
           fontsize: float = 30,
           pad: float = 15) -> None:
    ''' Add axes labels to a plot. '''
    assert type(fontsize) in [float, int]
    assert type(pad) in [float, int]

    if xlabel is not None:
        assert type(xlabel) == str
        ax.set_xlabel(xlabel, fontsize=fontsize, labelpad=pad)

    if ylabel is not None:
        assert type(ylabel) == str
        ax.set_ylabel(ylabel, fontsize=fontsize, labelpad=pad)


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
