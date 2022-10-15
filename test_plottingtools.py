"""Test suite for plottingtools.py"""

import matplotlib.figure  # type: ignore
import matplotlib.pyplot as plt  # type: ignore
import pytest

import plottingtools as pt

######################
# General Aesthetics #
######################


def test_tex_on_off():
    pt.texon()
    pt.texoff()


def test_light_and_darkmode():
    pt.lightmode()
    pt.darkmode()


####################
# Types of layouts #
####################


def test_singleplot():
    fig, _ = pt.singleplot(size=(7, 5))
    assert isinstance(fig, matplotlib.figure.Figure)
    plt.close()


def test_multiplot():
    _, _ = pt.multiplot(nrows=3, ncols=2, size_xy=(20, 12), hspace=1, wspace=1)
    plt.close()


#############################
# Adding elements to a plot #
#############################


def test_legend():
    _, ax = pt.singleplot()
    pt.legend(ax, loc="upper left", fontsize=20, frame=True)
    plt.close()


def test_legend_pathological():
    with pytest.raises(ValueError):
        pt.legend("not an ax object")


def test_title():
    _, ax = pt.singleplot()
    pt.title(ax, "abcdef", fontsize=25, pad=10)
    assert ax.get_title() == "abcdef"
    plt.close()


def test_title_pathological():
    with pytest.raises(ValueError):
        pt.title("not an ax object", "abcdef", fontsize=25, pad=10)


def test_labels():
    _, ax = pt.singleplot()
    pt.labels(ax, xlabel="xlabel", ylabel="ylabel", fontsize=10, pad=5)
    assert ax.get_xlabel() == "xlabel"
    assert ax.get_ylabel() == "ylabel"
    plt.close()


def test_labels_pathological():
    with pytest.raises(ValueError):
        pt.labels("not an ax object",
                  xlabel="xlabel",
                  ylabel="ylabel",
                  fontsize=10,
                  pad=5)


def test_diagonal():
    _, ax = pt.singleplot()
    pt.diagonal(ax)
    plt.close()


def test_diagonal_pathological():
    with pytest.raises(ValueError):
        pt.diagonal("not an ax object")


def test_rectangle():
    _, ax = pt.singleplot()
    pt.rectangle(ax,
                 x1=1,
                 x2=2,
                 y1=1,
                 y2=2,
                 linewidth=3,
                 linestyle=":",
                 fill=True)
    plt.close()


def test_rectangle_pathological():
    with pytest.raises(ValueError):
        pt.rectangle("not an ax object",
                     x1=1,
                     x2=2,
                     y1=1,
                     y2=2,
                     linewidth=3,
                     linestyle=":",
                     fill=True)

    _, ax = pt.singleplot()
    with pytest.raises(ValueError):
        pt.rectangle(ax,
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
    _, ax = pt.singleplot()
    pt.despine(ax, ['top', 'left', 'bottom', 'right'])
    plt.close()


def test_despine_pathological():
    with pytest.raises(ValueError):
        pt.despine("not an ax object")


def test_respine():
    _, ax = pt.singleplot()
    pt.respine(ax, ['top', 'left', 'bottom', 'right'])
    plt.close()


def test_respine_pathological():
    with pytest.raises(ValueError):
        pt.respine("not an ax object")


def test_ticklabelsize():
    _, ax = pt.singleplot()
    pt.ticklabelsize(ax, size=25)
    plt.close()


def test_ticklabelsize_pathological():
    with pytest.raises(ValueError):
        pt.ticklabelsize("not an ax object")


def test_limits():
    _, ax = pt.singleplot()
    pt.limits(ax, xlimits=(3, 5), ylimits=None)
    pt.limits(ax, xlimits=None, ylimits=(4, 6))
    assert ax.get_xlim() == (3, 5)
    assert ax.get_ylim() == (4, 6)
    plt.close()


def test_limits_pathological():
    with pytest.raises(ValueError):
        pt.limits("not an ax object", xlimits=(3, 5), ylimits=None)


def test_ticks_and_labels():
    _, ax = pt.singleplot()
    pt.ticks_and_labels(ax, which="x", ticks=[-0.14, 1, 2], ticklabels=None)
    pt.ticks_and_labels(ax, which="y", ticks=[-0.14, 1, 2], ticklabels=None)
    pt.ticks_and_labels(ax, which="xy", ticks=[-0.14, 1, 2], ticklabels=None)
    pt.ticks_and_labels(ax, which="yx", ticks=[-0.14, 1, 2], ticklabels=None)
    plt.close()


def test_ticks_and_labels_pathological():
    _, ax = pt.singleplot()
    with pytest.raises(ValueError):
        pt.ticks_and_labels(ax,
                            which="aaaaaaaaaaaaaaa",
                            ticks=[-0.14, 1, 2],
                            ticklabels=None)
    plt.close()

    with pytest.raises(ValueError):
        pt.ticks_and_labels("not an ax object",
                            which="yx",
                            ticks=[-0.14, 1, 2],
                            ticklabels=None)


@pytest.mark.filterwarnings('ignore::UserWarning')
def test_rotate_ticklabels():
    _, ax = pt.singleplot()
    pt.rotate_ticklabels(ax, which="x", rotation=10.5)
    pt.rotate_ticklabels(ax, which="y", rotation=-10.5)
    pt.rotate_ticklabels(ax, which="xy", rotation=10.5)
    pt.rotate_ticklabels(ax, which="yx", rotation=-10.5)
    pt.rotate_ticklabels(ax, which="both", rotation=-10.5)
    plt.close()


@pytest.mark.filterwarnings('ignore::UserWarning')
def test_rotate_ticklabels_pathological():
    _, ax = pt.singleplot()
    with pytest.raises(ValueError):
        pt.rotate_ticklabels(ax, which="aaaaaaaaaaaaaaaa", rotation=10.5)
    plt.close()

    with pytest.raises(ValueError):
        pt.rotate_ticklabels("not an ax obj", which="x", rotation=10.5)


@pytest.mark.filterwarnings('ignore::UserWarning')
def test_align_ticklabels():
    _, ax = pt.singleplot()
    pt.align_ticklabels(ax, which="x", horizontal=None, vertical="center")
    pt.align_ticklabels(ax, which="y", horizontal=None, vertical="top")
    pt.align_ticklabels(ax, which="x", horizontal="right", vertical=None)
    pt.align_ticklabels(ax, which="y", horizontal="left", vertical=None)
    plt.close()


@pytest.mark.filterwarnings('ignore::UserWarning')
def test_align_ticklabels_pathological():
    _, ax = pt.singleplot()
    with pytest.raises(ValueError):
        pt.align_ticklabels(ax,
                            which="aaaaaaaaaaaaaaaa",
                            horizontal=None,
                            vertical="center")
    plt.close()

    with pytest.raises(ValueError):
        pt.align_ticklabels("not an ax obj",
                            which="x",
                            horizontal=None,
                            vertical="center")
