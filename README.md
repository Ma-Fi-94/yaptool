# yaptool

## What is it?
yaptool ("Yet Another Plotting Tool") is a library of plotting functions which I have been developing for some time now. The library is a collection of wrapper functions around the matplotlib library for Python. Its main purpose is the reduction of boilerplate code required for day-to-day tasks, as well as providing some aesthetically pleasing default parameter choices. Hence, the library is not a plotting library on its own, but a collection of functions intended to make data visualisation (such as for exploratory analysis and the communication of results) just a little bit easier. I use it myself on a (nearly) daily basis, and thus continuously test and develop it, It is, however, currently still in a rather early stage.

## An Example
Here's a little animation consisting of a series of plots which have been generated with the help of this library:

![](https://github.com/Ma-Fi-94/plottingtools/blob/main/docs/animation.gif)

## Quickstart
Just download the yaptool.py file and paste it either into the folder of your project, or into your Python libraries folder.

Consider the following little Python snippet as an example of how to use it:

```python3
import yaptool as yap

# Activate dark mode and TeX support
yap.darkmode()
yap.texon()

# Make a new plot
fig, ax = yap.singleplot()

# Plot some data using matplotlib
ax.scatter([1,2,3,4], [6,9,13,21])
ax.plot([0,6], [0,30], c="C1", ls=":")

# Set ax limits in one single line of code
yap.limits(ax, (0,5), (0,25))

# Remove top and right spine, again in one single line of code
yap.despine(ax)

# Enlarge the font size of the tick labels (again only one LoC)
yap.ticklabelsize(ax)

# Label axes. Note that TeX syntax is possible, since we activated TeX mode earlier. (yet another one-liner!)
yap.labels(ax, "$x$", "$f(x)$")

# Export figure to file
yap.save_svg("Test.svg")
```

This yields the following figure:
![](https://github.com/Ma-Fi-94/plottingtools/blob/main/docs/Test.svg)

## Overview over Features
- Light- and dark mode
- TeX support
- Make single- and multi plot figures with one line of code
- Easily beautify matplotlib plots using convenience functions with sensible, aesthetically pleasing default choices:
  - Despine plots, change tick positions and labels, change ticklabel size, change axis limits, change tick label rotation, change tick label alignment -- with one single line of code each
  - Add (or change) title, axis labels, rectangles, lines, etc. with one single line of code each
- Export current figure to PNG, SVG or PDF with one single line of code

## Is there a documentation?
Yes! Although it is currently being written, and thus still a bit WIP-y. You can find it here: https://github.com/Ma-Fi-94/yaptool/blob/main/docs . To generate the docs yourself, use `pdoc yaptool.py -d google -o ./docs` or just run `make docs`.
