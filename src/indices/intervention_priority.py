import pandas as pd

from ..utils.scoring_helpers import weighted_sum
from ..config import parameters, thresholds


def compute_intervention_priority(
    sri_df: pd.DataFrame,
    cbr_df: pd.DataFrame
) -> pd.DataFrame:
    """
    Computes Intervention Priority Ranking (IPR).

    Enforces:
    - Monthly aggregation
    - One-to-one merge
    - Policy-configured thresholds
    """

    # Enforce monthly uniqueness
    sri_monthly = (
        sri_df
        .groupby(["region_id", "month"], as_index=False)
        .agg({"sri_score": "mean"})
    )

    cbr_monthly = (
        cbr_df
        .groupby(["region_id", "month"], as_index=False)
        .agg({"cbr_score": "mean"})
    )

    # Safe one-to-one merge
    data = pd.merge(
        sri_monthly,
        cbr_monthly,
        on=["region_id", "month"],
        how="inner",
        validate="one_to_one"
    )

    # Priority score
    data["priority_score"] = weighted_sum(
        data[["sri_score", "cbr_score"]],
        weights=parameters["IPR_WEIGHTS"]
    )

    # Decision thresholds (from config)
    ipr_thresholds = thresholds["IPR"]

    escalate = ipr_thresholds["ESCALATE"]
    intervene = ipr_thresholds["INTERVENE"]

    def classify(score):
        if score >= escalate:
            return "Escalate"
        elif score >= intervene:
            return "Intervene"
        else:
            return "Monitor"

    data["recommended_action"] = data["priority_score"].apply(classify)

    return data
