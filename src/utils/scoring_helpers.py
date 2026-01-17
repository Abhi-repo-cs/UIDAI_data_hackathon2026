import numpy as np
import pandas as pd


def validate_weights(weights: dict, columns: list):
    """
    Validates that:
    - All required columns have weights
    - Weights sum approximately to 1
    """

    missing = set(columns) - set(weights.keys())
    if missing:
        raise ValueError(
            f"Missing weights for columns: {missing}"
        )

    total_weight = sum(weights.values())
    if not np.isclose(total_weight, 1.0, atol=0.05):
        raise ValueError(
            f"Weights must sum to 1. Current sum: {total_weight}"
        )


def weighted_sum(
    df: pd.DataFrame,
    weights: dict
) -> pd.Series:
    """
    Computes a weighted sum across columns.

    Assumes inputs are already normalized.
    Missing values are treated as zero-risk signals.
    """

    validate_weights(weights, df.columns.tolist())

    score = pd.Series(0, index=df.index)

    for column, weight in weights.items():
        score += df[column].fillna(0) * weight

    return score
