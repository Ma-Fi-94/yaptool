import matplotlib.pyplot as plt  # type: ignore
import matplotlib.figure  # type: ignore
import numpy as np

import pytest
import sys
import io

import plottingtools as pt


def test_singleplot():
    fig, ax = pt.singleplot()
    assert type(fig) == matplotlib.figure.Figure

    fig, ax = pt.singleplot(size=(7, 5))
    assert type(fig) == matplotlib.figure.Figure

    fig, ax = pt.singleplot(size=[7, 5])
    assert type(fig) == matplotlib.figure.Figure


def test_singleplot_pathological():
    with pytest.raises(AssertionError) as exception_info:
        pt.singleplot(size=1)
    with pytest.raises(AssertionError) as exception_info:
        pt.singleplot(size="abc")
    with pytest.raises(AssertionError) as exception_info:
        pt.singleplot(size=(1, "abc"))
    with pytest.raises(AssertionError) as exception_info:
        pt.singleplot(size=("abc", 1))


def test_title():
    fig, ax = pt.singleplot()
    pt.title(ax, "abcdef")
    assert ax.get_title() == "abcdef"


def test_title_pathological():
    fig, ax = pt.singleplot()
    with pytest.raises(AssertionError) as exception_info:
        pt.title(ax, title=123)
    with pytest.raises(AssertionError) as exception_info:
        pt.title(ax, title="title", fontsize="abc")
    with pytest.raises(AssertionError) as exception_info:
        pt.title(ax, title="title", pad="abc")
    #with pytest.raises(AssertionError) as exception_info:
    #	pt.title(ax=123, title="title")


def test_labels():
    fig, ax = pt.singleplot()
    pt.labels(ax, xlabel="xlabel", ylabel="ylabel")
    assert ax.get_xlabel() == "xlabel"
    assert ax.get_ylabel() == "ylabel"


def test_labels_pathological():
    fig, ax = pt.singleplot()
    with pytest.raises(AssertionError) as exception_info:
        pt.labels(ax, xlabel="xlabel", ylabel="label", pad="abc")
    with pytest.raises(AssertionError) as exception_info:
        pt.labels(ax, xlabel="xlabel", ylabel="label", fontsize="abc")
    with pytest.raises(AssertionError) as exception_info:
        pt.labels(ax, xlabel="xlabel", ylabel=123)
    with pytest.raises(AssertionError) as exception_info:
        pt.labels(ax, xlabel=123, ylabel="ylabel")
    #with pytest.raises(AssertionError) as exception_info:
    #	pt.labels(ax="abc", xlabel="xlabel", ylabel="ylabel")


def test_despine():
    fig, ax = pt.singleplot()
    pt.despine(ax, ['top', 'left', 'bottom', 'right'])


def test_despine_pathological():
    fig, ax = pt.singleplot()
    with pytest.raises(AssertionError) as exception_info:
        pt.despine(ax, which=['bla'])
    with pytest.raises(AssertionError) as exception_info:
        pt.despine(ax, which=123)
    #with pytest.raises(AssertionError) as exception_info:
    #	pt.despine(ax="abc", which=["left"])


def test_ticklabelsize():
    fig, ax = pt.singleplot()
    pt.ticklabelsize(ax, size=25)


def test_ticklabelsize_pathological():
    fig, ax = pt.singleplot()
    #with pytest.raises(AssertionError) as exception_info:
    #	pt.ticklabelsize(ax, size="abc")


def test_limits():
    fig, ax = pt.singleplot()
    pt.limits(ax, xlimits=(3, 5), ylimits=None)
    pt.limits(ax, xlimits=None, ylimits=(4, 6))
    assert ax.get_xlim() == (3, 5)
    assert ax.get_ylim() == (4, 6)


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
