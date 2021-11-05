import matplotlib.pyplot as plt  # type: ignore
import matplotlib.figure  # type: ignore
import numpy as np

import pytest
import sys
import io

import plottingtools as pt


def test_light_and_darkmode():
    pt.lightmode()
    pt.darkmode()


def test_singleplot():
    fig, ax = pt.singleplot()
    assert type(fig) == matplotlib.figure.Figure

    fig, ax = pt.singleplot(size=(7, 5))
    assert type(fig) == matplotlib.figure.Figure

    fig, ax = pt.singleplot(size=[7, 5])
    assert type(fig) == matplotlib.figure.Figure
    plt.close()


def test_singleplot_pathological():
    with pytest.raises(AssertionError) as exception_info:
        pt.singleplot(size=1)
    with pytest.raises(AssertionError) as exception_info:
        pt.singleplot(size="abc")
    with pytest.raises(AssertionError) as exception_info:
        pt.singleplot(size=(1, "abc"))
    with pytest.raises(AssertionError) as exception_info:
        pt.singleplot(size=("abc", 1))
    plt.close()


def test_title():
    fig, ax = pt.singleplot()
    pt.title(ax, "abcdef", fontsize=25, pad=10)
    assert ax.get_title() == "abcdef"
    plt.close()


def test_title_pathological():
    fig, ax = pt.singleplot()
    with pytest.raises(AssertionError) as exception_info:
        pt.title(ax, title=123)
    with pytest.raises(AssertionError) as exception_info:
        pt.title(ax, title="title", fontsize="abc")
    with pytest.raises(AssertionError) as exception_info:
        pt.title(ax, title="title", fontsize=-54321)
    with pytest.raises(AssertionError) as exception_info:
        pt.title(ax, title="title", pad="abc")
    #with pytest.raises(AssertionError) as exception_info:
    #	pt.title(ax=123, title="title")
    plt.close()


def test_labels():
    fig, ax = pt.singleplot()
    pt.labels(ax, xlabel="xlabel", ylabel="ylabel", fontsize=10, pad=5)
    assert ax.get_xlabel() == "xlabel"
    assert ax.get_ylabel() == "ylabel"
    plt.close()


def test_labels_pathological():
    fig, ax = pt.singleplot()
    with pytest.raises(AssertionError) as exception_info:
        pt.labels(ax, xlabel="xlabel", ylabel="label", pad="abc")
    with pytest.raises(AssertionError) as exception_info:
        pt.labels(ax, xlabel="xlabel", ylabel="label", fontsize="abc")
    with pytest.raises(AssertionError) as exception_info:
        pt.labels(ax, xlabel="xlabel", ylabel="label", fontsize=-5)
    with pytest.raises(AssertionError) as exception_info:
        pt.labels(ax, xlabel="xlabel", ylabel=123)
    with pytest.raises(AssertionError) as exception_info:
        pt.labels(ax, xlabel=123, ylabel="ylabel")
    #with pytest.raises(AssertionError) as exception_info:
    #	pt.labels(ax="abc", xlabel="xlabel", ylabel="ylabel")
    plt.close()


def test_despine():
    fig, ax = pt.singleplot()
    pt.despine(ax, ['top', 'left', 'bottom', 'right'])
    plt.close()


def test_despine_pathological():
    fig, ax = pt.singleplot()
    with pytest.raises(AssertionError) as exception_info:
        pt.despine(ax, which=['bla'])
    with pytest.raises(AssertionError) as exception_info:
        pt.despine(ax, which=123)
    #with pytest.raises(AssertionError) as exception_info:
    #	pt.despine(ax="abc", which=["left"])
    plt.close()


def test_ticklabelsize():
    fig, ax = pt.singleplot()
    pt.ticklabelsize(ax, size=25)
    plt.close()


def test_ticklabelsize_pathological():
    fig, ax = pt.singleplot()
    with pytest.raises(AssertionError) as exception_info:
        pt.ticklabelsize(ax, size="abc")
    plt.close()


def test_limits():
    fig, ax = pt.singleplot()
    pt.limits(ax, xlimits=(3, 5), ylimits=None)
    pt.limits(ax, xlimits=None, ylimits=(4, 6))
    assert ax.get_xlim() == (3, 5)
    assert ax.get_ylim() == (4, 6)
    plt.close()


def test_limits_pathological():
    fig, ax = pt.singleplot()
    with pytest.raises(AssertionError) as exception_info:
        pt.limits(ax, xlimits=12345, ylimits=None)
    with pytest.raises(AssertionError) as exception_info:
        pt.limits(ax, xlimits=None, ylimits=12345)
    with pytest.raises(AssertionError) as exception_info:
        pt.limits(ax, xlimits=[12345], ylimits=None)
    with pytest.raises(AssertionError) as exception_info:
        pt.limits(ax, xlimits=None, ylimits=[12345])
    with pytest.raises(AssertionError) as exception_info:
        pt.limits(ax, xlimits=[12345, "abc"], ylimits=None)
    with pytest.raises(AssertionError) as exception_info:
        pt.limits(ax, xlimits=None, ylimits=[12345, "def"])
    plt.close()


def test_diagonal():
    fig, ax = pt.singleplot()
    pt.diagonal(ax)
    plt.close()


def test_diagonal_pathological():
    fig, ax = pt.singleplot()
    with pytest.raises(AssertionError) as exception_info:
        pt.diagonal(ax, alpha="abc")
    with pytest.raises(AssertionError) as exception_info:
        pt.diagonal(ax, alpha=-1234)
    with pytest.raises(AssertionError) as exception_info:
        pt.diagonal(ax, linestyle="abc")
    with pytest.raises(AssertionError) as exception_info:
        pt.diagonal(ax, linestyle=1234)
    with pytest.raises(AssertionError) as exception_info:
        pt.diagonal(ax, linewidth=-1234)
    with pytest.raises(AssertionError) as exception_info:
        pt.diagonal(ax, colour=-1234)
    plt.close()


def test_rectangle():
    fig, ax = pt.singleplot()
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
    fig, ax = pt.singleplot()
    with pytest.raises(AssertionError) as exception_info:
        pt.rectangle(ax, x1="abc", x2=2, y1=1, y2=2)
    with pytest.raises(AssertionError) as exception_info:
        pt.rectangle(ax, x1=1, x2="abc", y1=1, y2=2)
    with pytest.raises(AssertionError) as exception_info:
        pt.rectangle(ax, x1=1, x2=2, y1="abc", y2=2)
    with pytest.raises(AssertionError) as exception_info:
        pt.rectangle(ax, x1=1, x2=2, y1=1, y2="abc")
    with pytest.raises(AssertionError) as exception_info:
        pt.rectangle(ax, x1=1, x2=2, y1=1, y2=2, colour=-1234)
    with pytest.raises(AssertionError) as exception_info:
        pt.rectangle(ax, x1=1, x2=2, y1=1, y2=2, linewidth=-1234)
    with pytest.raises(AssertionError) as exception_info:
        pt.rectangle(ax, x1=1, x2=2, y1=1, y2=2, linestyle=-1234)
    with pytest.raises(AssertionError) as exception_info:
        pt.rectangle(ax, x1=1, x2=2, y1=1, y2=2, fill="abcde")
    plt.close()


def test_star():
    fig, ax = pt.singleplot()
    pt.star(ax, x=1, y=2, colour="blue", fontsize=25)
    plt.close()


def test_star_pathological():
    fig, ax = pt.singleplot()
    with pytest.raises(AssertionError) as exception_info:
        pt.star(ax, x="abc", y=2)
    with pytest.raises(AssertionError) as exception_info:
        pt.star(ax, x=1, y="abc")
    with pytest.raises(AssertionError) as exception_info:
        pt.star(ax, x=1, y=2, colour=-123)
    plt.close()


def test_ax_ticks_and_labels():
    fig, ax = pt.singleplot()
    pt.ax_ticks_and_labels(ax, which="x", ticks=[-0.14, 1, 2], labels=None)
    pt.ax_ticks_and_labels(ax, which="y", ticks=[-0.14, 1, 2], labels=None)
    pt.ax_ticks_and_labels(ax, which="xy", ticks=[-0.14, 1, 2], labels=None)
    pt.ax_ticks_and_labels(ax, which="yx", ticks=[-0.14, 1, 2], labels=None)


def test_ax_ticks_and_labels_pathological():
    fig, ax = pt.singleplot()

    with pytest.raises(AssertionError) as exception_info:
        pt.ax_ticks_and_labels(ax,
                               which="x",
                               ticks=[-0.14, 1, 2, "a"],
                               labels=None)
    with pytest.raises(AssertionError) as exception_info:
        pt.ax_ticks_and_labels(ax,
                               which="y",
                               ticks=[-0.14, 1, 2, 3.5],
                               labels=["a"])
    with pytest.raises(AssertionError) as exception_info:
        pt.ax_ticks_and_labels(ax,
                               which="abc",
                               ticks=[-0.14, 1, 2, 3.5],
                               labels=["a", "b", "c"])
    plt.close()

def test_similarity_matrix():
    pass
