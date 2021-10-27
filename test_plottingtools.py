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
