import matplotlib as mpl

def configure_matplotlib():
    grey = '#666666'
    lw = 0.5
    margin = 0.15
    mpl.rcParams['figure.figsize'] = (5,5)
    mpl.rcParams['font.size'] = 9
    mpl.rcParams['font.sans-serif'].insert(0,'Open Sans')
    mpl.rcParams['legend.fontsize'] = 'medium'
    mpl.rcParams['lines.linewidth'] = lw
    mpl.rcParams['patch.linewidth'] = lw
    mpl.rcParams['axes.linewidth'] = lw
    mpl.rcParams['patch.edgecolor'] = grey
    mpl.rcParams['axes.edgecolor'] = grey
    mpl.rcParams['axes.labelcolor'] = grey
    mpl.rcParams['text.color'] = grey
    mpl.rcParams['xtick.color'] = grey
    mpl.rcParams['ytick.color'] = grey
    mpl.rcParams['xtick.major.size'] = 3
    mpl.rcParams['xtick.minor.size'] = 1
    mpl.rcParams['xtick.major.width'] = 0.3
    mpl.rcParams['xtick.minor.width'] = 0.3
    mpl.rcParams['ytick.major.size'] = 3
    mpl.rcParams['ytick.minor.size'] = 1
    mpl.rcParams['ytick.major.width'] = 0.3
    mpl.rcParams['ytick.minor.width'] = 0.3
    mpl.rcParams['figure.subplot.left'] = margin
    mpl.rcParams['figure.subplot.right'] = 1-margin
    mpl.rcParams['figure.subplot.bottom'] = margin
    mpl.rcParams['figure.subplot.top'] = 1-margin
    mpl.rcParams['figure.subplot.wspace'] = 2*margin
    mpl.rcParams['figure.subplot.hspace'] = 2*margin
