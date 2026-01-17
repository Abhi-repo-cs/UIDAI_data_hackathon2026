import pandas as pd


def rolling_std(series: pd.Series, window: int) -> pd.Series:
    """
    Computes rolling standard deviation.

    - Backward-looking window
    - min_periods=1 ensures early data is retained
    - Used to capture demand volatility
    """

    return (
        series
        .rolling(window=window, min_periods=1)
        .std()
        .fillna(0)
    )


def rolling_mean(series: pd.Series, window: int) -> pd.Series:
    """
    Computes rolling mean.

    Used for smoothing baseline demand.
    """

    return (
        series
        .rolling(window=window, min_periods=1)
        .mean()
        .fillna(0)
    )


def rolling_median(series: pd.Series, window: int) -> pd.Series:
    """
    Computes rolling median.

    More robust than mean for peak detection.
    """

    return (
        series
        .rolling(window=window, min_periods=1)
        .median()
        .fillna(0)
    )

