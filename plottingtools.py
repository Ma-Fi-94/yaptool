import matplotlib.pyplot as plt

####################
# Types of layouts #
####################

def singleplot(size=(10,7)):
	''' Make a new 10x7 plot. Size can also be changed. '''
    
    # TODO: check if size is tuple or list or array of 2 integers
    fig, ax = plt.subplots(1, 1, figsize=size)       
	return fig, ax




# TODO: more defensive programming for all of these below

#############################
# Adding elements to a plot #
#############################

def labels(ax, xlabel=None, ylabel=None, fontsize=30, pad=15):
	''' Add axes labels to a plot. '''
	if xlabel is not None:
		ax.set_xlabel(xlabel, fontsize=fontsize, labelpad=pad)
	if ylabel is not None:
		ax.set_ylabel(ylabel, fontsize=fontsize, labelpad=pad)


def title(ax, title, fontsize=40, pad=20):
	''' Add a title to a plot. '''
	ax.set_title(title, fontsize=fontsize, pad=pad)


#############################
# Change elements of a plot #
#############################

def despine(ax, which=['top', 'right']):
	''' Remove spines of ax object. Spines can be specified, default is top and right. '''
	for spine in which:
		ax.spines[spine].set_visible(False)


def limits(ax, xlimits=None, ylimits=None):
	''' Set axes limits of ax object. '''
	if xlimits is not None:
		ax.set_xlim(xlimits)
	if ylimits is not None:
		ax.set_ylim(ylimits)


def ticklabelsize(ax, which="both", axis="both", size=20):
	''' Change ticklabelsize of an ax object. '''
	ax.tick_params(which=which, axis=axis, labelsize=size)
