# plottingtools

## What is it?
plottingtools is a library of plotting functions which I have been developing for some time now. The library is mostly a collection of wrapper functions around the matplotlib library for Python. Its main purpose is the reduction of boilerplate code required for day-to-day tasks, as well as providing some aesthetically pleasing default parameter choices. Hence, the library is not a plotting library on its own, but a collection of functions intended to make data visualisation (such as for exploratory analysis and the communication of results) just a little bit easier :).

## Quickstart
Just download the plottingtools.py file and paste it either into the folder of your project, or into your Python libraries folder.

Consider the following little Python snippet as an example of how to use it:

```python3
import plottingtools as pt

# Activate dark mode and TeX support
pt.darkmode()
pt.texon()

# Make a new plot
fig, ax = pt.singleplot()

# Plot some data
# (Dedicated library functions for this are currently being written, too)
ax.scatter([1,2,3,4], [6,9,13,21])
ax.plot([0,6], [0,30], c="C1", ls=":")

# Set ax limits in one single line of code
pt.limits(ax, (0,5), (0,25))

# Remove top and right spine, again in one single line of code
pt.despine(ax)

# Enlarge the font size of the tick labels (again only one LoC)
pt.ticklabelsize(ax)

# Label axes. Note that TeX syntax is possible, since we activated TeX mode earlier. (yet another one-liner!)
pt.labels(ax, "$x$", "$f(x)$")

# Export figure to file
pt.save_svg("Test.svg")
```

This yields the following figure:
![](https://github.com/Ma-Fi-94/plottingtools/blob/main/docs/Test.svg)

## Is there a documentation?
Yes! Although it is currently being written, and thus still a bit WIP-y. You can find it here: https://github.com/Ma-Fi-94/plottingtools/blob/main/docs/plottingtools.pdf. Feel free to check it out to learn about a bunch of other cool features I have already implemented ;).
