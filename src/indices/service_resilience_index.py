import pandas as pd
import numpy as np

from src.utils.rolling_windows import rolling_std, rolling_median
from src.utils.normalization import zscore_normalize
from src.utils.scoring_helpers import weighted_sum
from src.config import parameters, thresholds


def compute_service_resilience_index(df: pd.DataFrame) -> pd.DataFrame:
    """
    Computes the Service Resilience Index (SRI).

    Higher SRI score = lower resilience.
    """

    # ✅ FIX: copy() MUST be called
    data = df.copy()

    # --------------------------------------------------
    # Step 1: Total service demand
    # --------------------------------------------------
    data["total_demand"] = (
        data["enrolments"] + data["biometric_updates"]
    )

    window = parameters["ROLLING_WINDOW_MONTHS"]

    # --------------------------------------------------
    # Step 2: Demand volatility
    # --------------------------------------------------
    data["volatility"] = (
        data
        .groupby("region_id")["total_demand"]
        .transform(lambda x: rolling_std(x, window))
    )

    # --------------------------------------------------
    # Step 3: Demand acceleration
    # --------------------------------------------------
    data["growth_rate"] = (
        data
        .groupby("region_id")["total_demand"]
        .pct_change()
    )

    data["acceleration"] = (
        data
        .groupby("region_id")["growth_rate"]
        .diff()
        .abs()
    )

    # --------------------------------------------------
    # Step 4: Peak-to-baseline intensity
    # --------------------------------------------------
    data["baseline"] = (
        data
        .groupby("region_id")["total_demand"]
        .transform(lambda x: rolling_median(x, window))
    )

    data["peak_intensity"] = (
        data["total_demand"] / data["baseline"].replace(0, np.nan)
    ).fillna(0)

    # --------------------------------------------------
    # Step 5: Normalize signals
    # --------------------------------------------------
    data["volatility_norm"] = zscore_normalize(data["volatility"])
    data["acceleration_norm"] = zscore_normalize(data["acceleration"])
    data["peak_norm"] = zscore_normalize(data["peak_intensity"])

    # --------------------------------------------------
    # Step 6: Composite SRI score
    # --------------------------------------------------
    data["sri_score"] = weighted_sum(
        data[["volatility_norm", "acceleration_norm", "peak_norm"]],
        weights=parameters["SRI_WEIGHTS"]
    )

    # --------------------------------------------------
    # Step 7: Categorization
    # --------------------------------------------------
    data["sri_category"] = np.select(
        [
            data["sri_score"] < thresholds["SRI"]["STABLE"],
            data["sri_score"] < thresholds["SRI"]["VULNERABLE"]
        ],
        [
            "Stable",
            "Vulnerable"
        ],
        default="Fragile"
    )

    return data[
        [
            "region_id",
            "month",
            "sri_score",
            "sri_category"
        ]
    ]
