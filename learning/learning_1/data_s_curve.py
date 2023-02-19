def data_S_curve(path2):
  from sklearn import manifold, datasets
  import pandas as pd

  n_samples = 1500
  S_points, S_color = datasets.make_s_curve(n_samples, random_state=0)

  x, y, z = S_points.T

  # get the list of tuples from two lists.
  # and merge them by using zip().
  list_of_tuples = list(zip(x, y, z, S_color))

  df = pd.DataFrame(list_of_tuples,
                  columns=['x1', 'x2', 'x3', 'S_color'])
  df.to_csv(path2,index=False)
