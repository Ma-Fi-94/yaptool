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
        
