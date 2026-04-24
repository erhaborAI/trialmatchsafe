# Abstract

Clinical trial eligibility screening is often treated as a binary classification task, in which patients are labeled as eligible or not eligible based on structured or unstructured criteria. However, real-world clinical decision-making operates under conditions of uncertainty, incomplete information, and varying levels of risk. Systems that do not explicitly account for these factors may produce decisions that are technically correct but clinically unsafe or misleading.

We present TrialMatchSafe, a safety-aware clinical AI system that reframes trial eligibility screening as a safety-sensitive decision problem. The system separates baseline eligibility determination from a safety-gated decision layer that evaluates whether a decision is safe to act upon. This architecture enables explicit handling of missing information, uncertainty, and clinically relevant exclusion risk that may not be reliably captured through simple rule matching.

TrialMatchSafe consists of three core components: 
(1) a criteria parsing module that converts free-text trial eligibility descriptions into structured inclusion and exclusion rules; 
(2) a patient feature extraction module that derives clinically relevant attributes from unstructured patient summaries; and 
(3) a dual-layer decision framework comprising a baseline eligibility classifier and a safety-gated controller. The safety gate produces one of three actions—ALLOW, DEFER, or ESCALATE—depending on the presence of violated criteria, uncertainty, or high-risk signals.

The system provides transparent, criterion-level reasoning and explicitly surfaces decision uncertainty, enabling more interpretable and clinically aligned outputs. Through this design, TrialMatchSafe demonstrates how clinical AI systems can move beyond performance-focused evaluation toward safety-aware decision support that better reflects real-world clinical workflows.

This work highlights the necessity of incorporating safety constraints and uncertainty modeling into clinical AI systems and provides a conceptual and practical foundation for more reliable deployment of AI in high-stakes healthcare decision environments.
