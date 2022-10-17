"""Test suite for plottingtools.py"""

import matplotlib.figure  # type: ignore
import matplotlib.pyplot as plt  # type: ignore
import pytest

import yaptool as yap

######################
# General Aesthetics #
######################


def test_tex_on_off():
    """Test turning TeX mode on and off."""
    yap.texon()
    yap.texoff()


def test_light_and_darkmode():
    """Test switiching to lightmode and darkmode."""
    yap.lightmode()
    yap.darkmode()


####################
# Types of layouts #
####################


def test_singleplot():
    """Test making a new single plot figure."""
    fig, _ = yap.singleplot(size=(7, 5))
    assert isinstance(fig, matplotlib.figure.Figure)
    plt.close()


def test_multiplot():
    """Test making a new multi plot figure."""
    _, _ = yap.multiplot(nrows=3,
                         ncols=2,
                         size_xy=(20, 12),
                         hspace=1,
                         wspace=1)
    plt.close()


#############################
# Adding elements to a plot #
#############################


def test_legend():
    """Test adding a legend."""
    _, ax = yap.singleplot()
    yap.legend(ax, loc="upper left", fontsize=20, frame=True)
    plt.close()


def test_legend_pathological():
    """Pathological tests for adding a legend."""
    with pytest.raises(ValueError):
        yap.legend("not an ax object")


def test_title():
    """Test adding a title."""
    _, ax = yap.singleplot()
    yap.title(ax, "abcdef", fontsize=25, pad=10)
    assert ax.get_title() == "abcdef"
    plt.close()


def test_title_pathological():
    """Pathological test for adding a title."""
    with pytest.raises(ValueError):
        yap.title("not an ax object", "abcdef", fontsize=25, pad=10)


def test_labels():
    """Test adding ax labels."""
    _, ax = yap.singleplot()
    yap.labels(ax, xlabel="xlabel", ylabel="ylabel", fontsize=10, pad=5)
    assert ax.get_xlabel() == "xlabel"
    assert ax.get_ylabel() == "ylabel"
    plt.close()


def test_labels_pathological():
    """Pathological test for adding ax labels."""
    with pytest.raises(ValueError):
        yap.labels("not an ax object",
                   xlabel="xlabel",
                   ylabel="ylabel",
                   fontsize=10,
                   pad=5)


def test_diagonal():
    """Test adding diagonal."""
    _, ax = yap.singleplot()
    yap.diagonal(ax)
    plt.close()


def test_diagonal_pathological():
    """Pathological test for adding diagonal."""

    with pytest.raises(ValueError):
        yap.diagonal("not an ax object")


def test_rectangle():
    """Test adding a rectangle."""
    _, ax = yap.singleplot()
    yap.rectangle(ax,
                  x1=1,
                  x2=2,
                  y1=1,
                  y2=2,
                  linewidth=3,
                  linestyle=":",
                  fill=True)
    plt.close()


def test_rectangle_pathological():
    """Pathological test for adding a rectangle."""

    with pytest.raises(ValueError):
        yap.rectangle("not an ax object",
                      x1=1,
                      x2=2,
                      y1=1,
                      y2=2,
                      linewidth=3,
                      linestyle=":",
                      fill=True)

    _, ax = yap.singleplot()
    with pytest.raises(ValueError):
        yap.rectangle(ax,
                      x1="not a number",
                      x2=2,
                      y1=1,
                      y2=2,
                      linewidth=3,
                      linestyle=":",
                      fill=True)
    plt.close()


#############################
# Change elements of a plot #
#############################


def test_despine():
    """Test for despining."""
    _, ax = yap.singleplot()
    yap.despine(ax, ['top', 'left', 'bottom', 'right'])
    plt.close()


def test_despine_pathological():
    """Pathological test for despining."""
    with pytest.raises(ValueError):
        yap.despine("not an ax object")


def test_respine():
    """Test respining."""
    _, ax = yap.singleplot()
    yap.respine(ax, ['top', 'left', 'bottom', 'right'])
    plt.close()


def test_respine_pathological():
    """Pathological test for respining."""
    with pytest.raises(ValueError):
        yap.respine("not an ax object")


def test_ticklabelsize():
    """Test setting ticklabel size."""
    _, ax = yap.singleplot()
    yap.ticklabelsize(ax, size=25)
    plt.close()


def test_ticklabelsize_pathological():
    """Pathological test for setting ticklabel size."""
    with pytest.raises(ValueError):
        yap.ticklabelsize("not an ax object")


def test_limits():
    """Test setting ax limits."""
    _, ax = yap.singleplot()
    yap.limits(ax, xlimits=(3, 5), ylimits=None)
    yap.limits(ax, xlimits=None, ylimits=(4, 6))
    assert ax.get_xlim() == (3, 5)
    assert ax.get_ylim() == (4, 6)
    plt.close()


def test_limits_pathological():
    """Pathological test for setting ax limits."""
    with pytest.raises(ValueError):
        yap.limits("not an ax object", xlimits=(3, 5), ylimits=None)


def test_ticks_and_labels():
    """Test setting ax ticks and labels."""
    _, ax = yap.singleplot()
    yap.ticks_and_labels(ax, which="x", ticks=[-0.14, 1, 2], ticklabels=None)
    yap.ticks_and_labels(ax, which="y", ticks=[-0.14, 1, 2], ticklabels=None)
    yap.ticks_and_labels(ax, which="xy", ticks=[-0.14, 1, 2], ticklabels=None)
    yap.ticks_and_labels(ax, which="yx", ticks=[-0.14, 1, 2], ticklabels=None)
    plt.close()


def test_ticks_and_labels_pathological():
    """Pathological tests for setting ax ticks and labels."""
    _, ax = yap.singleplot()
    with pytest.raises(ValueError):
        yap.ticks_and_labels(ax,
                             which="aaaaaaaaaaaaaaa",
                             ticks=[-0.14, 1, 2],
                             ticklabels=None)
    plt.close()

    with pytest.raises(ValueError):
        yap.ticks_and_labels("not an ax object",
                             which="yx",
                             ticks=[-0.14, 1, 2],
                             ticklabels=None)


@pytest.mark.filterwarnings('ignore::UserWarning')
def test_rotate_ticklabels():
    """Test setting tick label rotation."""
    _, ax = yap.singleplot()
    yap.rotate_ticklabels(ax, which="x", rotation=10.5)
    yap.rotate_ticklabels(ax, which="y", rotation=-10.5)
    yap.rotate_ticklabels(ax, which="xy", rotation=10.5)
    yap.rotate_ticklabels(ax, which="yx", rotation=-10.5)
    yap.rotate_ticklabels(ax, which="both", rotation=-10.5)
    plt.close()


@pytest.mark.filterwarnings('ignore::UserWarning')
def test_rotate_ticklabels_pathological():
    """Pathological test for setting tick label rotation."""
    _, ax = yap.singleplot()
    with pytest.raises(ValueError):
        yap.rotate_ticklabels(ax, which="aaaaaaaaaaaaaaaa", rotation=10.5)
    plt.close()

    with pytest.raises(ValueError):
        yap.rotate_ticklabels("not an ax obj", which="x", rotation=10.5)


@pytest.mark.filterwarnings('ignore::UserWarning')
def test_align_ticklabels():
    """Test setting tick label alignments."""
    _, ax = yap.singleplot()
    yap.align_ticklabels(ax, which="x", horizontal=None, vertical="center")
    yap.align_ticklabels(ax, which="y", horizontal=None, vertical="top")
    yap.align_ticklabels(ax, which="x", horizontal="right", vertical=None)
    yap.align_ticklabels(ax, which="y", horizontal="left", vertical=None)
    plt.close()


@pytest.mark.filterwarnings('ignore::UserWarning')
def test_align_ticklabels_pathological():
    """Pathological test for setting tick label alignments."""
    _, ax = yap.singleplot()
    with pytest.raises(ValueError):
        yap.align_ticklabels(ax,
                             which="aaaaaaaaaaaaaaaa",
                             horizontal=None,
                             vertical="center")
    plt.close()

    with pytest.raises(ValueError):
        yap.align_ticklabels("not an ax obj",
                             which="x",
                             horizontal=None,
                             vertical="center")
