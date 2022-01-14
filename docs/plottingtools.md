# Publc Methods of "plottingtools", grouped by Topic

## General Aesthetics

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



## Adding elements to an existing plot







- Description

    - 

- Required parameters

    - 
    
- Optional parameters

    - **

- Return
    -


