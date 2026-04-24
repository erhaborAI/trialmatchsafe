import streamlit as st
import pandas as pd
from datetime import datetime

from core.criteria_parser import parse_criteria
from core.patient_parser import extract_patient_features
from core.matcher import evaluate_match
from core.safety_gate import apply_safety_gate, baseline_decision


st.set_page_config(
    page_title="TrialMatchSafe",
    page_icon="🧬",
    layout="wide"
)

st.title("TrialMatchSafe")
st.subheader("Safety-Aware Clinical Trial Matching with Uncertainty and Escalation")

st.write(
    "TrialMatchSafe is a prototype clinical AI safety system for trial eligibility screening. "
    "It compares a baseline eligibility decision with a safety-gated decision that explicitly handles "
    "missing information, exclusion risks, and uncertainty."
)

case_options = {
    "Likely eligible case": "data/case_eligible.txt",
    "Uncertain case": "data/case_uncertain.txt",
    "Not eligible case": "data/case_not_eligible.txt",
    "Edge case (uncertain / adversarial)": "data/case_edge.txt"
}

selected_case = st.selectbox("Choose a sample patient case", list(case_options.keys()))

with open(case_options[selected_case], "r") as f:
    sample_patient = f.read()

with open("data/sample_trial.txt", "r") as f:
    sample_trial = f.read()

col1, col2 = st.columns(2)

with col1:
    st.markdown("### Patient Summary")
    patient_text = st.text_area(
        "Paste patient summary here",
        value=sample_patient,
        height=300
    )

with col2:
    st.markdown("### Trial Eligibility Criteria")
    trial_text = st.text_area(
        "Paste trial criteria here",
        value=sample_trial,
        height=300
    )

if st.button("Evaluate Trial Match"):
    criteria = parse_criteria(trial_text)
    features = extract_patient_features(patient_text)
    match_results = evaluate_match(features, criteria)

    baseline = baseline_decision(match_results)
    gate = apply_safety_gate(match_results)

    st.markdown("---")
    st.markdown("## Baseline vs Safety-Gated Decision")

    col_a, col_b = st.columns(2)

    with col_a:
        st.markdown("### Baseline Eligibility Decision")
        if baseline["eligibility"] == "ELIGIBLE":
            st.success(baseline["eligibility"])
        else:
            st.error(baseline["eligibility"])
        st.write(f"**Reason:** {baseline['reason']}")
        st.caption("Baseline logic does not explicitly manage uncertainty or missing clinical information.")

    with col_b:
        st.markdown("### Safety-Gated Decision")
        if gate["decision"] == "ALLOW":
            st.success(gate["eligibility"])
        elif gate["decision"] == "DEFER":
            st.warning(gate["eligibility"])
        else:
            st.error(gate["eligibility"])

        st.write(f"**Safety Action:** {gate['decision']}")
        st.write(f"**Reason:** {gate['reason']}")
        st.write(f"**Unknown Criteria Count:** {gate['unknown_count']}")

    st.markdown("### Key Insight")

    baseline_allows = baseline["eligibility"] in ["ELIGIBLE", "LIKELY ELIGIBLE"]
    safety_blocks = gate["decision"] in ["DEFER", "ESCALATE"]

    if baseline_allows and safety_blocks:
        st.error(
            "The baseline decision would allow eligibility, but the safety gate blocks or escalates the case. "
            "This demonstrates a clinically important failure mode under uncertainty or exclusion risk."
        )
    elif gate["decision"] == "ALLOW":
        st.info(
            "Baseline and safety-gated decisions are aligned. The safety gate allows the case because no exclusion risks, violated inclusions, or unknown criteria were detected."
        )
    elif gate["decision"] == "DEFER":
        st.warning(
            "The safety gate defers this case because missing or uncertain information prevents a safe eligibility conclusion."
        )
    else:
        st.error(
            "The safety gate escalates this case because one or more exclusion risks were detected."
        )

    st.markdown("## Safety Review Summary")

    if gate["violated_exclusions"]:
        st.error("Exclusion risk detected.")
        for item in gate["violated_exclusions"]:
            st.write(f"- **{item['criterion']}**: {item['reason']}")

    if gate["violated_inclusions"]:
        st.warning("Required inclusion criterion not satisfied.")
        for item in gate["violated_inclusions"]:
            st.write(f"- **{item['criterion']}**: {item['reason']}")

    if gate["unknowns"]:
        st.warning("Missing or uncertain information detected.")
        for item in gate["unknowns"]:
            st.write(f"- **{item['criterion']}**: {item['reason']}")

    if not gate["violated_exclusions"] and not gate["violated_inclusions"] and not gate["unknowns"]:
        st.success("No exclusion risks, violated inclusions, or unknown criteria detected.")

    st.markdown("## Extracted Patient Features")
    st.json(features)

    st.markdown("## Parsed Trial Criteria")
    st.write("**Inclusion Criteria:**")
    st.write(criteria["inclusion"])
    st.write("**Exclusion Criteria:**")
    st.write(criteria["exclusion"])

    st.markdown("## Criterion-Level Eligibility Assessment")
    df = pd.DataFrame(match_results)
    st.dataframe(df, use_container_width=True)

    report = f"""
TrialMatchSafe Eligibility Report
Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}

Selected Case:
{selected_case}

Baseline Decision:
{baseline['eligibility']}
Reason: {baseline['reason']}

Safety-Gated Decision:
Eligibility: {gate['eligibility']}
Safety Action: {gate['decision']}
Reason: {gate['reason']}
Unknown Criteria Count: {gate['unknown_count']}

Patient Summary:
{patient_text}

Trial Criteria:
{trial_text}

Criterion-Level Assessment:
{df.to_string(index=False)}

Interpretation:
This system does not make an enrollment decision. It supports structured screening by identifying criteria that are satisfied, violated, or unknown, and by escalating cases where exclusion criteria or missing information could affect safe decision-making.
"""

    st.download_button(
        label="Download Eligibility Report",
        data=report,
        file_name="trialmatchsafe_report.txt",
        mime="text/plain"
    )

    st.markdown("## Interpretation")
    st.write(
        "TrialMatchSafe demonstrates how clinical trial matching can be treated as a safety-sensitive "
        "decision support problem rather than a simple text-matching task. The system separates baseline "
        "eligibility logic from a safety-gated layer that detects uncertainty, missing data, and exclusion risks."
    )