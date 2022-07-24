import matplotlib.pyplot as plt
plt.close('all')
import pandas as pd
import seaborn as sns
from statsmodels.tsa.api import acf, graphics, pacf
from statsmodels.tsa.ar_model import AutoReg, ar_select_order
import numpy as np


dat = pd.read_csv('avocado.csv')

regions = list(dat['region'].unique())

dat_tab = dat.groupby(['Date']).agg({'AveragePrice':'mean'})

dat_tab.reset_index(inplace = True, drop = False)

train = dat_tab[:-30]
test = dat_tab[-30:]

ar = AutoReg(train['AveragePrice'],lags = 20).fit()
print(ar.summary())
pred = ar.predict(train.shape[0],train.shape[0]+test.shape[0])

fig = plt.figure(1)
ax = fig.add_subplot(111)
ax.plot(dat_tab['AveragePrice'])
ax.plot(pred)

step = 10
xtick_labels = list(dat_tab['Date'])
xticks = np.arange(0,dat_tab.shape[0],step)
xtick_labels = xtick_labels[::step]

plt.xticks(xticks,xtick_labels, rotation = 45)

plt.tight_layout()


