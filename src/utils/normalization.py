import numpy as np
import pandas as pd


def zscore_normalize(series: pd.Series) -> pd.Series:
    """
    Z-score normalization with safety guards.

    Returns a normalized series where:
    mean = 0, std = 1

    If standard deviation is zero or data is missing,
    returns zeros to avoid artificial risk inflation.
    """

    mean = series.mean(skipna=True)
    std = series.std(skipna=True)

    if std == 0 or np.isnan(std):
        return pd.Series(0, index=series.index)

    return (series - mean) / std


def minmax_normalize(series: pd.Series) -> pd.Series:
    """
    Min-max normalization scaled to [0, 1].

    If max == min (flat signal), returns zeros.
    """

    min_val = series.min(skipna=True)
    max_val = series.max(skipna=True)

    if max_val == min_val or np.isnan(max_val):
        return pd.Series(0, index=series.index)

    return (series - min_val) / (max_val - min_val)


def normalize(series: pd.Series, method: str = "zscore") -> pd.Series:
    """
    Dispatcher function to normalize a series
    based on the configured method.
    """

    method = method.lower()

    if method == "zscore":
        return zscore_normalize(series)
    elif method == "minmax":
        return minmax_normalize(series)
    else:
        raise ValueError(
            f"Unsupported normalization method: {method}"
        )
