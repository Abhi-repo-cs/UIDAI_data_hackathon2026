import pandas as pd
from pathlib import Path

from src.indices.service_resilience_index import compute_service_resilience_index
from src.indices.continuity_break_risk import compute_continuity_break_risk
from src.indices.intervention_priority import compute_intervention_priority


def run_analysis():
    """
    Runs the full Aadhaar Continuity & Resilience analysis pipeline.

    This is the single source of truth for:
    - Loading processed data
    - Computing SRI, CBR, IPR
    - Producing decision-ready outputs
    """

    BASE_DIR = Path(__file__).resolve().parents[2]
    DATA_PATH = BASE_DIR / "data" / "processed" / "aadhaar_monthly_merged.csv"
    OUTPUT_PATH = BASE_DIR / "data" / "processed"

    # Load processed data
    df = pd.read_csv(DATA_PATH)

    # Compute indices
    sri_df = compute_service_resilience_index(df)
    cbr_df = compute_continuity_break_risk(df)
    ipr_df = compute_intervention_priority(sri_df, cbr_df)

    # Save outputs
    sri_df.to_csv(OUTPUT_PATH / "sri_output.csv", index=False)
    cbr_df.to_csv(OUTPUT_PATH / "cbr_output.csv", index=False)
    ipr_df.to_csv(OUTPUT_PATH / "ipr_output.csv", index=False)

    return sri_df, cbr_df, ipr_df


if __name__ == "__main__":
    run_analysis()
