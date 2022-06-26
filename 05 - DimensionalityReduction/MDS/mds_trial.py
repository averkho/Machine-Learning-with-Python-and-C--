
from numpy.random import RandomState
import matplotlib.pyplot as plt
from matplotlib import ticker
from utils import Utils

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

def plot_3d(points, points_color, title):
    x, y, z = points.T

    fig, ax = plt.subplots(
        tight_layout=True,
        subplot_kw={"projection": "3d"},
    )
    fig.suptitle(title, size=16)
    col = ax.scatter(x, y, z, color = Utils.green_hex, s=50, alpha=0.8)
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
    ax.tick_params(axis='x', colors=Utils.purple_hex,labelsize=15)
    ax.tick_params(axis='y', colors=Utils.purple_hex,labelsize=15)
    ax.tick_params(axis='z', colors=Utils.purple_hex,labelsize=15)
    plt.show()


def plot_2d(points, points_color, title):
    
    fig=plt.figure(2, figsize=(3, 3),)
    ax = fig.add_subplot(111)
    fig.suptitle(title, size=16)
    ax.scatter(points[:,0],points[:,1])
    plt.show()


def add_2d_scatter(ax, points, points_color, title=None):
    x, y = points.T
    ax.scatter(x, y, c=points_color, s=50, alpha=0.8)
    ax.set_title(title)
    ax.xaxis.set_major_formatter(ticker.NullFormatter())
    ax.yaxis.set_major_formatter(ticker.NullFormatter())


plot_3d(S_points, S_color,  "Original S-curve samples")

n_components = 2
md_scaling = manifold.MDS(
    n_components=n_components, max_iter=50, n_init=4, random_state=rng
)
S_scaling = md_scaling.fit_transform(S_points)

X,y = make_blobs(100,n_features = 3)
fig = plt.figure(2)
ax = fig.add_subplot(111)
plot_2d(S_scaling, S_color, "Multidimensional scaling")
