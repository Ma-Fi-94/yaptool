import matplotlib.pyplot as plt
import matplotlib.figure

import pytest
import plottingtools as pt



def test_singleplot():
    fig, ax = pt.singleplot()
    assert type(fig) == matplotlib.figure.Figure
