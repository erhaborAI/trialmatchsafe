# TrialMatchSafe

## Safety-Aware Clinical Trial Matching with Safety-Gated Decision Logic

A safety-aware clinical system for trial eligibility screening that explicitly models uncertainty, missing information, and escalation in high-stakes decisions.

[Open Live Demo](https://safe-triage-clinical-ai-6crggxq8gtkajbkzg6m2m.streamlit.app)

TrialMatchSafe is a prototype clinical system for safety-aware trial eligibility screening. It reframes trial matching from a binary classification task into a safety-sensitive decision problem under uncertainty.

The system separates baseline eligibility logic from a safety-gated decision layer that explicitly accounts for uncertainty, missing information, and clinically relevant exclusion risk.


---

## Motivation

Clinical trial matching is often framed as a straightforward classification problem: eligible or not eligible.

However, in real clinical settings:
- patient data may be incomplete
- exclusion risks may be subtle
- errors can lead to inappropriate enrollment or missed opportunities
- uncertainty is unavoidable

A system that outputs a binary decision without handling these factors can be unsafe.

TrialMatchSafe demonstrates a safer alternative:
**bounded, interpretable decision-making with explicit escalation pathways.**

---

## System Design

The system consists of three main components:

### 1. Criteria Parsing
- Converts free-text trial eligibility criteria into structured inclusion and exclusion rules

### 2. Patient Feature Extraction
- Extracts structured clinical variables from patient summaries
- Handles key attributes such as:
  - age
  - diagnoses
  - lab values
  - risk flags

### 3. Decision Layers

#### Baseline Decision
- Determines eligibility based on satisfied/violated criteria
- Does not account for uncertainty or missing data

#### Safety-Gated Decision
- Applies additional logic to detect:
  - violated exclusion criteria
  - unmet inclusion criteria
  - missing or uncertain information
- Produces one of three actions:
  - **ALLOW**
  - **DEFER**
  - **ESCALATE**

---

## Key Concept: Safety Gating

Instead of treating eligibility as a binary output, the system introduces a **safety gate** that governs whether a decision is safe to act upon.

This reflects real clinical workflows, where:
- uncertain cases require review
- high-risk signals trigger escalation
- not all decisions should be automated

---

## Example Outputs

For each case, the system provides:

- Baseline eligibility decision
- Safety-gated decision and action
- Explicit reasoning
- Criterion-level assessment table
- Extracted patient features
- Structured interpretation of system behavior

---

## Running the App

### Requirements

```bash
pip install -r requirements.txt
