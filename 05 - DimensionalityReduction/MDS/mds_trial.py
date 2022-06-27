
from numpy.random import RandomState
import matplotlib.pyplot as plt
from matplotlib import ticker
from utils import Utils
import numpy as np
import pandas as pd

np.random.seed(100)

from sklearn.datasets import make_blobs

import matplotlib.pyplot as plt
plt.close('all')
from matplotlib import cm

# unused but required import for doing 3d projections with matplotlib < 3.2
import mpl_toolkits.mplot3d  # noqa: F401

from sklearn import manifold, datasets

rng = RandomState(1)


n_samples = 1500
S_points, S_color = datasets.make_s_curve(n_samples, random_state=rng)

def plot_3d(i,points, points_color, title):
    x, y, z = points.T
    
    fig = plt.figure(i)
    
    ax = fig.add_subplot(111, projection = '3d')
    
    fig.suptitle(title, size=16)
    col = ax.scatter(x, y, z, c = points_color, s=50, alpha=0.8)
    fig.patch.set_facecolor(Utils.black_hex)
    ax.set_facecolor(Utils.black_hex)
    #ax.view_init(azim=-60, elev=9)
    ax.xaxis.set_major_locator(ticker.MultipleLocator(1))
    ax.yaxis.set_major_locator(ticker.MultipleLocator(1))
    ax.zaxis.set_major_locator(ticker.MultipleLocator(1))
    
    for spine in ax.spines.values():
        spine.set_edgecolor(Utils.white_hex)
        spine.set(linewidth=3)
    ax.spines['right'].set_visible(False)
    ax.spines['top'].set_visible(False)
    ax.set_title('',color=Utils.purple_hex,
                 fontproperties={'family':Utils.csfont,'size':20})
    # ax.tick_params(axis='x', colors=Utils.purple_hex,labelsize=15)
    # ax.tick_params(axis='y', colors=Utils.purple_hex,labelsize=15)
    # ax.tick_params(axis='z', colors=Utils.purple_hex,labelsize=15)
    plt.show()


def plot_2d(i,points, points_color, title):
    
    fig=plt.figure(i)
    ax = fig.add_subplot(111)
    fig.suptitle(title, size=16)
    ax.scatter(points[:,0],points[:,1], c = points_color)
    plt.show()


def add_2d_scatter(ax, points, points_color, title=None):
    x, y = points.T
    ax.scatter(x, y, c=points_color, s=50, alpha=0.8)
    ax.set_title(title)
    ax.xaxis.set_major_formatter(ticker.NullFormatter())
    ax.yaxis.set_major_formatter(ticker.NullFormatter())


plot_3d(1,S_points, S_color,  "Original S-curve samples")

n_components = 2
md_scaling = manifold.MDS(
    n_components=n_components, max_iter=50, n_init=4, random_state=rng
)
S_scaling = md_scaling.fit_transform(S_points)
plot_2d(2,S_scaling, S_color, "Multidimensional scaling")

X,y = make_blobs(500,n_features = 3)
S_scaling = md_scaling.fit_transform(X)
plot_3d(3,X, y,  "Original S-curve samples")
plot_2d(4,S_scaling, y, "Multidimensional scaling")

dat = pd.DataFrame(X,columns = ['x1','x2','x3'])
dat['y'] = y
dat.to_csv('./Data/mds_data.csv',index = False)
