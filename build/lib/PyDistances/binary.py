import polars as pl
import pandas as pd
from scipy.spatial import distance
from scipy.spatial.distance import pdist, squareform

################################################################################

def Sokal_dist_matrix(X):
    """
    Calculates the Sokal distance matrix for a data matrix `X` using SciPy.

    Parameters (inputs)
    ----------
    X: a pandas/polars DataFrame or a NumPy array. It represents a data matrix.

    Returns (outputs)
    -------
    M: the Sokal distance matrix between the rows of X.
    """
        
    if isinstance(X, pl.DataFrame):
        X = X.to_numpy()
    if isinstance(X, pd.DataFrame):
        X = X.to_numpy()    

    # Compute the pairwise distances using pdist and convert to a square form.
    M = squareform(pdist(X, metric='sokalmichener'))
    
    return M

################################################################################

def Sokal_dist(xi, xr) :
    """
    Calculates the Sokal distance between a pair of vectors.

    Parameters (inputs)
    ----------
    xi, xr: a pair of quantitative vectors. They represent a couple of statistical observations.

    Returns (outputs)
    -------
    The Sokal distance between the observations `xi` and `xr`.
    """
    return distance.sokalmichener(xi, xr)

################################################################################

def Jaccard_dist_matrix(X):
    """
    Calculates the Jaccard distance matrix for a data matrix `X` using SciPy.

    Parameters (inputs)
    ----------
    X: a pandas/polars DataFrame or a NumPy array. It represents a data matrix.

    Returns (outputs)
    -------
    M: the Jaccard distance matrix between the rows of X.
    """

    if isinstance(X, pl.DataFrame):
        X = X.to_numpy()
    if isinstance(X, pd.DataFrame):
        X = X.to_numpy()    

    # Compute the pairwise distances using pdist and convert to a square form.
    M = squareform(pdist(X, metric='jaccard'))
    
    return M

################################################################################

def Jaccard_dist(xi, xr) :
    """
    Calculates the Jaccard distance between a pair of vectors.

    Parameters (inputs)
    ----------
    xi, xr: a pair of quantitative vectors. They represent a couple of statistical observations.

    Returns (outputs)
    -------
    The Jaccard distance between the observations `xi` and `xr`.
    """
    return distance.jaccard(xi, xr)

################################################################################


