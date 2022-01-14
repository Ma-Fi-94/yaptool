# Publc Methods of "plottingtools", grouped by Topic

## Changing the colour theme

### **plottingtools.lightmode([foreground = "0", background = "1.0"])**
- Description

    - Switch to light theme.

- Required parameters

    - None.
    
- Optional parameters

    - *foreground* String specifying the foreground colour. Default: "0", i.e. pure black.
    - *background* String specifying the background colour. Default: "1.0", i.e. pure white.

- Return
    - None

### **plottingtools.darkmode([foreground = "0.85", background = "0.15"])**
- Description

    - Switch to dark theme.

- Required parameters

    - None.
    
- Optional parameters

    - *foreground* String specifying the foreground colour. Default: "0.85", i.e. light grey.
    - *background* String specifying the background colour. Default: "0.15", i.e. dark grey.

- Return
    - None


<div style="page-break-after: always;"></div>


## Making a new Figure

### **plottingtools.singleplot([size = (10, 7)])**
- Description

    - Generate a new plot with one figure.

- Required parameters

    - None.
    
- Optional parameters

    - *size* 2-Tuple of numbers, containing the figure's width and height. Default: (10, 7)

- Return
    - 2-tuple (matplotlib.figure.Figure, matplotlib.pyplot.Axes)

### **plottingtools.multiplot(nrows, ncols, size)**
- Description

    - Returns a figure with nrows by ncols subplots

- Required parameters

    - *nrows* integer, the number of rows of plots 
    - *ncols* integer, the number of columns of plots
    - *size_xy* 2-tuple of numbers, containing the figure's width and height
    
- Optional parameters

    - None.

- Return
    - Tuple (matplotlib.figure.Figure, matplotlib.pyplot.Axes)

<div style="page-break-after: always;"></div>

## Kinds of Plots unique to plottingtools

### **plottingtools.similarity_heatmap(ax, list_of_lists, method)**

- Description

    - 

- Required parameters

    - 
    
- Optional parameters

    - **

- Return
    - None.

### **plottingtools.correlations_heatmap(ax, list_of_lists, method)**

- Description

    - 

- Required parameters

    - 
    
- Optional parameters

    - **

- Return
    - None.


### **plottingtools.masked_heatmap(ax, data, mask, \*\*kwargs)**

- Description

    - 

- Required parameters

    - 
    
- Optional parameters

    - **

- Return
    - None.

<div style="page-break-after: always;"></div>

## Adding elements to an existing plot
### **plottingtools.title(ax, title, [fontsize = 40, pad = 20])**

- Description

    - 

- Required parameters

    - 
    
- Optional parameters

    - **

- Return
    - None.

### **plottingtools.labels(ax, xlabel, ylabel, [fontsize = 30, pad = 15])**

- Description

    - 

- Required parameters

    - 
    
- Optional parameters

    - **

- Return
    - None.

### **plottingtools.diagonal(ax, [colour = "black", alpha = 0.3, linestyle = "-", linewidth = 2])**

- Description

    - 

- Required parameters

    - 
    
- Optional parameters

    - **

- Return
    - None.

### **plottingtools.rectangle(ax, x1, y1, x2, y2, [colour = "red", linewidth = 3, linestyle = "-", fill = False])**

- Description

    - 

- Required parameters

    - 
    
- Optional parameters

    - **

- Return
    - None.

### **plottingtools.star(ax, x, y, [colour = "red", fontsize = 50])**

- Description

    - 

- Required parameters

    - 
    
- Optional parameters

    - **

- Return
    - None.

### **plottingtools.lines(ax, which, pos, [colour = "black", alpha = 0.3, linestyle = "-", linewidth = 2, zorder = -100])**

- Description

    - 

- Required parameters

    - 
    
- Optional parameters

    - **

- Return
    - None.

<div style="page-break-after: always;"></div>

## Changing elements of a plot

### **plottingtools.despine(ax, [which = ['top', 'right']])**

- Description

    - Remove spines of a matplotlib.pyplot.Axes plot.

- Required parameters

    - *ax* The matplotlib.pyplot.Axes object to remove spines from.
    
- Optional parameters

    - *which* Array of strings specifying which spines to remove. Possible choices are "top", "right", "left", "bottom". Defaults to ["top", "right"].

- Return
    - None.

### **plottingtools.ticklabelsize(ax, [which = "both", size = 20])**

- Description

    - 

- Required parameters

    - 
    
- Optional parameters

    - **

- Return
    - None.

### **plottingtools.limits(ax, xlimits, ylimits)**

- Description

    - 

- Required parameters

    - 
    
- Optional parameters

    - **

- Return
    - None.

### **plottingtools.ticks_and_labels(ax, which, ticks, label)**

- Description

    - 

- Required parameters

    - 
    
- Optional parameters

    - **

- Return
    - None.

### **plottingtools.rotate_ticklabels(ax, which, rotation)**

- Description

    - 

- Required parameters

    - 
    
- Optional parameters

    - **

- Return
    - None.

### **plottingtools.align_ticklabels(ax, which, horizontal, vertical)**

- Description

    - 

- Required parameters

    - 
    
- Optional parameters

    - **

- Return
    - None.

<div style="page-break-after: always;"></div>

## Saving the current figure to a file
### **plottingtools.save_png(filename, [dpi = 300])**

- Description

    - Save the current plot as PNG file.

- Required parameters

    - *filename* string with the file name to export to.
    
- Optional parameters

    - *dpi* The resolution, in dpi. Default: 300

- Return
    - None.

### **plottingtools.save_svg(filename)**

- Description

    - Save the current plot as SVG file.

- Required parameters

    - *filename* string with the file name to export to.
    
- Optional parameters

    - None

- Return
    - None.


### **plottingtools.save_pdf(filename)**

- Description

    - Save the current plot as PDF file.

- Required parameters

    - *filename* string with the file name to export to.
    
- Optional parameters

    - None.

- Return
    - None.

<div style="page-break-after: always;"></div>

## Collections of default parameters for matplotlib plots
T.B.D.


 
