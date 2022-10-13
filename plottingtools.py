import matplotlib  # type: ignore
import matplotlib.pyplot as plt  # type: ignore
import matplotlib.figure  # type: ignore
from matplotlib.patches import Rectangle  # type: ignore
from matplotlib import rc  # type: ignore
import types

from typing import Tuple, List, Optional

####################
# Internal helpers #
####################

LINESTYLES = ["-", "--", "-.", ":"]


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

""" General aesthetics """

def darkmode(foreground: Optional[str] = "0.85",
             background: Optional[str] = "0.15") -> None:
    """Switches to dark mode. Foreground and background colours may also be specified explicitly.
    
    Args:
        foreground:
            An optional string, specifying the foreground colour, following matplotlib's colour syntax. Defaults to "0.85", i.e. light grey.
        background:
            An optional string, specifying the background colour, following matplotlib's colour syntax. Defaults to "0.15", i.e. dark grey.
    
    Returns:
        None
    """
    _set_fgbg(fg=foreground, bg=background)


def lightmode(foreground: Optional[str] = "0",
              background: Optional[str] = "1.0") -> None:
    """Switches to light mode. Foreground and background colours may also be specified explicitly.
    
    Args:
        foreground:
            An optional string, specifying the foreground colour, following matplotlib's colour syntax. Defaults to "0", i.e. black.
        background:
            An optional string, specifying the background colour, following matplotlib's colour syntax. Defaults to "1.0", i.e. white.
    
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


def singleplot(size: Optional[Tuple[float, float]] = (10, 7)) -> Tuple[matplotlib.figure.Figure, plt.Axes]:
    """Generates a new single-plot figure. The figure size may be defined explicitly.
    
    Args:
        size:
            An optional tuple of two floats, containing the desired figure width and heigth in inches. Defaults to 10x7 inches.
    
    Returns:
        fig:
            A matplotlib.figure.Figure instance
        ax:
            A pyplot.Axes instance
    """
    try:
        w, h = size
        w = float(w)
        h = float(h)
    except:
        raise AssertionError

    fig, ax = plt.subplots(1, 1, figsize=size)
    return fig, ax


def multiplot(
        nrows: int,
        ncols: int,
        size_xy: Tuple[float, float],
        wspace: Optional[float] = None,
        hspace: Optional[float] = None) -> Tuple[matplotlib.figure.Figure, plt.Axes]:
    """Generates a new figure consisting of nrows rows and ncols columns of plots with overall figure size size_xy. Horizontal and vertical distance between plots may be defined explicitly.
    
    Args:
        size:
            An tuple of two floats, containing the desired figure width and heigth in inches.
        wspace:
            An optional float, specifying the horizontal distance between columns. Defaults to zero.
        hspace:
            An optional float, specifying the vertical distance between rows. Defaults to zero.
    
    Returns:
        fig:
            A matplotlib.figure.Figure instance
        ax:
            An array of pyplot.Axes instances
    """    
    
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

    fig, ax = plt.subplots(nrows, ncols, figsize=(l, h))
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
          fontsize: Optional[float] = 30,
          pad: Optional[float] = 20) -> None:
    """Adds a title to an existing plot.
    
    Args:
        ax:
            A pyplot.Axes instance
        title:
            A string containing the title to add.
        fontsize:
            An optional float, specifying the font size of the title. Defaults to 30.
        pad:
            An optional float, specifying the padding between title and figure. Defaults to 20.
    
    Returns:
        None
    """    
    
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
           xlabel: Optional[str] = None,
           ylabel: Optional[str] = None,
           fontsize: Optional[float] = 30,
           pad: Optional[float] = 15) -> None:
    """Adds axes labels to an existing plot.
    
    Args:
        ax:
            A pyplot.Axes instance
        xlabel:
            An optional string containing the label to be added to the x-axis of the plot.
        ylabel:
            An optional string containing the label to be added to the y-axis of the plot.
        fontsize:
            An optional float, specifying the font size of the labels. Defaults to 30.
        pad:
            An optional float, specifying the padding between labels and figure. Defaults to 15.
    
    Returns:
        None
    """
    
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
             colour: Optional[str] = "black",
             alpha: Optional[float] = 0.3,
             linestyle: Optional[str] = "-",
             linewidth: Optional[float] = 2) -> None:
    """Adds the 45 degrees diagonal to an existing plot.
    
    Args:
        ax:
            A pyplot.Axes instance
        colour:
            An optional string containing the colour of the diagonal to be added. Defaults to "black".
        alpha:
            An optional float containing the alpha (opacity) of the diagonal to be added. Defaults to 0.3.
        linestyle:
            An optional string, specifying the line style of the diagonal to be added, Defaults to "-", i.e. a continuous line.
        linewidth:
            An optional float, specifying the width (in px) of the diagonal to be added. Defaults to 2.
    
    Returns:
        None
    """

    try:
        colour = str(colour)
        alpha = float(alpha)
        linewidth = float(linewidth)
    except:
        raise AssertionError

    assert (alpha >= 0) and (alpha <= 1)
    assert linestyle in LINESTYLES
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
              **kwargs) -> None:
    """Convenience function for addig a rectangle to an existing plot without having to manually call ax.add_patch(). Takes x and y coordinates of two points as arguments, instead of the x and y coordinate of one point and the rectagle width and heigth, like add_patch() would.
    
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
            Named arguments such as color, fill, linewidth, linestyle. Passed to ax.add_patch().
    
    Returns:
        None
    """    try:
        x1 = float(x1)
        y1 = float(y1)
        x2 = float(x2)
        y2 = float(y2)
    except:
        raise AssertionError
    assert hasattr(ax, 'plot')

    ax.add_patch(
        Rectangle((x1, y1),
                  x2 - x1,
                  y2 - y1,
                  **kwargs))

######################################## annotations properly done until this line #########################

def legend(ax, loc="best", fontsize=25, frame=False, **kwargs) -> None:
    ''' Add a legend to a plot. '''

    try:
        fontsize = float(fontsize)
        frame = bool(frame)
    except:
        raise AssertionError

    assert loc in [
        1, 2, 3, 4, 5, 6, 7, 8, "best", "upper right", "upper left",
        "lower left", "lower right", "right", "center left", "center right",
        "lower center", "upper center", "center"
    ]
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


#############################
# Change elements of a plot #
#############################


def despine(ax: plt.Axes,
            which: Optional[List[str]] = ['top', 'right']) -> None:
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


def ticklabelsize(ax: plt.Axes,
                  which: Optional[str] = "both",
                  size: Optional[float] = 30) -> None:
    ''' Change ticklabelsize of an ax object. '''
    try:
        size = float(size)
    except:
        raise AssertionError

    assert which in ["x", "y", "both"]
    assert hasattr(ax, 'plot')

    ax.tick_params(which, labelsize=size)


def limits(ax: plt.Axes,
           xlimits: Optional[Tuple[float, float]] = None,
           ylimits: Optional[Tuple[float, float]] = None) -> None:
    ''' Set axes limits of ax object. '''

    assert hasattr(ax, 'plot')
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

def ticks_and_labels(ax: plt.Axes,
                     which: str,
                     ticks: List[float],
                     labels: Optional[List[str]] = None) -> None:
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


def rotate_ticklabels(ax: plt.Axes,
                      which: str,
                      rotation: float) -> None:
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


def align_ticklabels(ax: plt.Axes,
                     which: str,
                     horizontal: Optional[str] = None,
                     vertical: Optional[str] = None) -> None:
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


##################
# Export figures #
##################


def save_png(filename: str,
             dpi: Optional[float] = 300) -> None:
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


def save_svg(filename: str) -> None:
    ''' Save current figure as svg file. '''
    try:
        filename = str(filename)
    except:
        raise AssertionError

    assert filename != ""
    plt.savefig(filename, bbox_inches="tight",
                format="svg")  # pragma: no cover


def save_pdf(filename: str) -> None:
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

def minorline(ax, x, y, linewidth=1, linestyle=":", **kwargs):
    ax.plot(x, y, lw=linewidth, ls=linestyle, **kwargs)

def oligoscatter(ax, x, y, marker="o", alpha=1, **kwargs):
    ax.scatter(x, y, marker=marker, alpha=alpha, **kwargs)

def polyscatter(ax, x, y, marker=".", alpha=0.5, **kwargs):
    ax.scatter(x, y, marker=marker, alpha=alpha, **kwargs)
