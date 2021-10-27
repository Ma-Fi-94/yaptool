import matplotlib.pyplot as plt
import matplotlib.figure
import numpy as np

import pytest
import plottingtools as pt



def test_singleplot():
    fig, ax = pt.singleplot()
    assert type(fig) == matplotlib.figure.Figure

    fig, ax = pt.singleplot(size=(7,5))
    assert type(fig) == matplotlib.figure.Figure

    fig, ax = pt.singleplot(size=[7,5])
    assert type(fig) == matplotlib.figure.Figure

    fig, ax = pt.singleplot(size=np.array([7,5]))
    assert type(fig) == matplotlib.figure.Figure

def test_singleplot_pathological():
    fig, ax = pt.singleplot(size=1)
    assert fig == None
    assert ax == None
    # TODO: test output too
