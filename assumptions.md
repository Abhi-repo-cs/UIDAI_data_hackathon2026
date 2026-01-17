Assumptions, Proxies, and Limitations

This project is designed as a decision-support system, not an automation or enforcement mechanism. The following assumptions and limitations are explicitly acknowledged to ensure transparency and trust.

Data & Scope Assumptions

Aggregated data only: All analysis is performed on aggregated UIDAI datasets. No individual-level Aadhaar data is used or inferred.

Single-state pilot: Due to download constraints, the current implementation uses Puducherry as a pilot. The framework is extensible to all states without structural changes.

Temporal granularity: Monthly aggregation is assumed sufficient to capture service stress and continuity risk trends.

Proxy Limitations

Service capacity proxies: Enrolment and biometric update volumes are used as indirect indicators of service load and stress. Actual centre-level capacity is not observed.

Lifecycle inference: Age-banded enrolment and update data are used as proxies for children nearing biometric update thresholds. Exact birthdays or eligibility dates are not available.

Geographic resolution: PIN or district identifiers are treated as service regions, not as precise representations of enrolment centre distribution.

Forecasting & Risk Interpretation

Risk bands, not predictions: Outputs represent relative risk levels and time-to-risk signals, not deterministic forecasts of failure.

No counterfactual enforcement: Simulated “post-intervention” scenarios are illustrative, intended to demonstrate directional impact rather than guaranteed outcomes.

Governance & Ethics Safeguards

No individual identification or tracking

No automated denial or eligibility decisions

Designed strictly for human-in-the-loop policy planning

These limitations are not weaknesses; they reflect responsible, governance-aligned analytics appropriate for national digital public infrastructure.