Preprocess data passed to pcolormesh so that axes are aligned to the centers of the corresponding rectangles, not their borders.

Example usage:

```python
import numpy as np
import matplotlib.pyplot as plt

from pcolormesh_preprocess import pcmp

x = np.linspace(-1,1)
y = np.linspace(-1,1)
xv, yv = np.meshgrid(x, y, sparse=False, indexing='ij')
data = xv**2 + yv**2/4

plt.pcolormesh(*pcmp(x,y,data))
plt.show()
```

If you prefer Cartesian indexing instead of matrix indexing (see documentation of np.meshgrid), you can use

```python
import numpy as np
import matplotlib.pyplot as plt

from pcolormesh_preprocess import pcmp_xy as pcmp

x = np.linspace(-1,1)
y = np.linspace(-1,1)
xv, yv = np.meshgrid(x, y, sparse=False, indexing='xy')
data = xv**2 + yv**2/4

plt.pcolormesh(*pcmp(x,y,data))
plt.show()
```

In both cases, the axes can also be omitted (then the axes are automatically generated with `np.arange`):

```python
plt.pcolormesh(*pcmp(data))
```
