# TrialMatchSafe

## Safety-Aware Clinical Trial Matching with Safety-Gated Decision Logic

A safety-aware clinical AI system for trial eligibility screening that explicitly models uncertainty, missing information, and escalation in high-stakes decisions.

---

## Live Demo
[Launch Interactive Demo](https://trialmatchsafe-83zrhvy9wghad7oaz4zvnb.streamlit.app/)

Explore how safety constraints reshape clinical eligibility decisions under uncertainty.

---

## Project Brief
[Download One-Page Project Brief (PDF)](TrialMatchSafe_Clinical_AI_Safety_Framework.pdf)

TrialMatchSafe is a prototype clinical AI system for safety-aware trial eligibility screening. It reframes trial matching from a binary classification task into a safety-sensitive decision problem under uncertainty.

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

## Running the App Locally

### Requirements

```bash
pip install -r requirements.txt
```

### Launch

```bash
streamlit run app.py
```
---

## Abstract

Clinical trial eligibility screening is often treated as a binary classification task, in which patients are labeled as eligible or not eligible based on structured or unstructured criteria. However, real-world clinical decision-making operates under conditions of uncertainty, incomplete information, and varying levels of risk. Systems that do not explicitly account for these factors may produce decisions that are technically correct but clinically unsafe or misleading.

TrialMatchSafe reframes trial eligibility screening as a safety-sensitive decision problem. The system separates baseline eligibility determination from a safety-gated decision layer that evaluates whether a decision is safe to act upon, enabling explicit handling of missing information, uncertainty, and clinically relevant exclusion risks.

The architecture consists of three components: criteria parsing, patient feature extraction, and a dual-layer decision framework combining baseline classification with a safety-gated controller. The system produces one of three actions—ALLOW, DEFER, or ESCALATE—based on detected risks and uncertainty.

This approach demonstrates how clinical AI systems can move beyond performance-focused evaluation toward safety-aware decision support that better reflects real-world clinical workflows.
