import numpy as np

def pcmp(*args, indexing="ij"):
  """
    Preprocess data passed to pcolormesh so that axes are aligned to the centers of the corresponding rectangles, not their borders.
    You can either call it with three arguments (x axis, y axis, 2D data) or with only one argument (only 2D data, x and y are generated
    automatically with np.arange).
    The indexing argument can be "ij" or "xy" to be compatible with data produced by np.meshgrid (see documentation of np.meshgrid).
    Returns a tuple (X,Y,C) that can serve as the first three arguments for matplotlib.pyplot.pcolormesh.
  """

  try:
    x,y,data = args
    x, y = x.reshape(-1), y.reshape(-1)
  except ValueError:
    data, = args
    x, y = np.arange(data.shape[0]), np.arange(data.shape[1])
    if indexing=="xy": x,y = y,x

  if indexing not in ["ij","xy"]: raise ValueError("indexing argument must be 'ij' or 'xy'")
  if indexing=="ij": data = data.T

  if x.size<2 or y.size<2: raise ValueError("axes must have a minimum length of 2")
  if not data.shape==(y.size, x.size): raise ValueError("axis sizes ({:d} and {:d}) incompatible with data shape {}".format(x.size, y.size, data.shape))

  xp = np.empty(x.size+1)
  yp = np.empty(y.size+1)

  xp[1:-1] = (x[1:] + x[:-1])/2
  xp[0] = x[0] - (xp[1]-x[0])
  xp[-1] = x[-1] + (x[-1] - xp[-2])

  yp[1:-1] = (y[1:] + y[:-1])/2
  yp[0] = y[0] - (yp[1]-y[0])
  yp[-1] = y[-1] + (y[-1] - yp[-2])

  return xp, yp, data

pcmp_xy = lambda *args: pcmp(*args, indexing="xy")
