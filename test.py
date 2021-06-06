# %%

import numpy as np
import matplotlib.pyplot as plt

from pcolormesh_preprocess import pcmp

x = np.linspace(-.5,.5,50)
y = np.linspace(-1,1,100)
xv, yv = np.meshgrid(x, y, sparse=False, indexing='ij')
data = xv**2 + yv**2/4

plt.figure()
plt.pcolormesh(*pcmp(x,y,data))
plt.gca().set_aspect("equal")

plt.figure()
plt.pcolormesh(*pcmp(data))

plt.show()

# %%

import numpy as np
import matplotlib.pyplot as plt

from pcolormesh_preprocess import pcmp_xy as pcmp

x = np.linspace(-.5,.5,50)
y = np.linspace(-1,1,100)
xv, yv = np.meshgrid(x, y, sparse=False, indexing='xy')
data = xv**2 + yv**2/4

plt.figure()
plt.pcolormesh(*pcmp(x,y,data))
plt.gca().set_aspect("equal")

plt.figure()
plt.pcolormesh(*pcmp(data))

plt.show()
