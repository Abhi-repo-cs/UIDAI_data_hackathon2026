Aadhaar Niranthar

UIDAI Data Hackathon 2026

Problem Statement

Aadhaar is not only an identity system but a continuity-dependent public infrastructure. Even when enrolment numbers appear healthy, Aadhaar usability can silently break due to delayed biometric updates, lifecycle transitions (especially among children), or fragile service delivery capacity. These failures often surface only when citizens face authentication denial or exclusion from services. The core question this project addresses is: Where is Aadhaar continuity likely to break in the next 6–12 months, and can the system absorb that risk before citizens are affected?

Method Overview

This project builds a predictive, decision-support system using only aggregated UIDAI datasets. Instead of descriptive volume analysis, we construct three interpretable, governance-ready indices:

Service Resilience Index (SRI) – Measures whether Aadhaar service delivery can absorb demand shocks, using demand volatility, acceleration, and peak-to-baseline stress rather than raw load.

Continuity Break Risk (CBR) – Estimates where Aadhaar usability is likely to fail due to delayed biometric updates and lifecycle transitions, particularly among children nearing mandatory update thresholds.

Intervention Priority Ranking (IPR) – Combines SRI and CBR into a ranked, decision-grade priority list indicating where UIDAI action will prevent maximum future exclusion.

All outputs are risk bands and priority signals—not deterministic predictions—ensuring interpretability and policy defensibility.

Key Findings

Continuity risk emerges before visible service stress
Several periods show elevated Continuity Break Risk despite moderate enrolment volumes, indicating that silent exclusion risks precede observable infrastructure overload.

Lifecycle-driven risk dominates biometric continuity failure
Child-linked age cohorts (5–15 years) contribute disproportionately to future continuity risk, highlighting the need for anticipatory, not reactive, biometric update strategies.

Resilience and continuity must be managed jointly
Districts or periods with moderate service resilience but rising continuity risk represent the highest leverage points for preventive intervention.

Ranked Action Recommendations (Illustrative)

Escalate – Initiate targeted, time-bound biometric update drives linked to schools and registrars where IPR is highest.

Intervene – Augment temporary service capacity and outreach in vulnerable but recoverable regions.

Monitor – Maintain surveillance where resilience is stable and continuity risk remains low.

Policy Relevance

This system reframes Aadhaar management from reactive service delivery to preventive continuity governance. The outputs are designed to integrate into monthly UIDAI operational reviews, enabling early action before exclusion occurs.