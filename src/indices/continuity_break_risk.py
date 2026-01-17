import pandas as pd
import numpy as np

from src.utils.rolling_windows import rolling_mean
from src.utils.normalization import zscore_normalize
from src.utils.scoring_helpers import weighted_sum
from src.config import parameters, thresholds


def compute_continuity_break_risk(
    df: pd.DataFrame
) -> pd.DataFrame:
    """
    Computes Continuity Break Risk (CBR).

    CBR estimates the risk that Aadhaar becomes unusable
    due to delayed biometric updates and lifecycle pressure.

    Higher CBR score = higher continuity failure risk.
    """

    data = df.copy()

    # --------------------------------------------------
    # Step 1: Construct enrolment-update backlog
    # --------------------------------------------------
    data["backlog_gap"] = (
        data["enrolments"] - data["biometric_updates"]
    ).clip(lower=0)

    # --------------------------------------------------
    # Step 2: Backlog growth rate (directional risk)
    # --------------------------------------------------
    data["backlog_growth"] = (
        data
        .groupby("region_id")["backlog_gap"]
        .diff()
        .fillna(0)
    )

    # --------------------------------------------------
    # Step 3: Lifecycle pressure proxy
    # Uses rolling enrolment intensity as proxy
    # --------------------------------------------------
    window = parameters["ROLLING_WINDOW_MONTHS"]

    data["enrolment_intensity"] = (
        data
        .groupby("region_id")["enrolments"]
        .transform(lambda x: rolling_mean(x, window))
    )

    # Relative pressure signal
    data["lifecycle_pressure"] = (
        data["enrolment_intensity"] /
        data.groupby("region_id")["enrolment_intensity"].transform("median")
    ).replace([np.inf, -np.inf], 0).fillna(0)

    # --------------------------------------------------
    # Step 4: Normalize signals
    # --------------------------------------------------
    data["backlog_gap_norm"] = zscore_normalize(data["backlog_gap"])
    data["backlog_growth_norm"] = zscore_normalize(data["backlog_growth"])
    data["lifecycle_norm"] = zscore_normalize(data["lifecycle_pressure"])

    # --------------------------------------------------
    # Step 5: Composite CBR score
    # --------------------------------------------------
    data["cbr_score"] = weighted_sum(
        data[
            [
                "backlog_gap_norm",
                "backlog_growth_norm",
                "lifecycle_norm"
            ]
        ],
        weights=parameters["CBR_WEIGHTS"]
    )

    # --------------------------------------------------
    # Step 6: Risk bands (policy-facing)
    # --------------------------------------------------
    data["risk_band"] = np.select(
        [
            data["cbr_score"] < thresholds["CBR"]["LOW"],
            data["cbr_score"] < thresholds["CBR"]["EMERGING"],
            data["cbr_score"] < thresholds["CBR"]["ELEVATED"]
        ],
        [
            "Low",
            "Emerging",
            "Elevated"
        ],
        default="Critical"
    )

    return data[
        [
            "region_id",
            "month",
            "cbr_score",
            "risk_band"
        ]
    ]
