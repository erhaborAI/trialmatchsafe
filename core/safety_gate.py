def apply_safety_gate(match_results):
    unknowns = [r for r in match_results if r["status"] == "UNKNOWN"]

    violated_inclusions = [
        r for r in match_results
        if r["type"] == "Inclusion" and r["status"] == "VIOLATED"
    ]

    violated_exclusions = [
        r for r in match_results
        if r["type"] == "Exclusion" and r["status"] == "VIOLATED"
    ]

    if violated_exclusions:
        return {
            "decision": "ESCALATE",
            "eligibility": "NOT ELIGIBLE",
            "reason": "One or more exclusion criteria appear to be present and require manual review.",
            "unknown_count": len(unknowns),
            "violated_exclusions": violated_exclusions,
            "violated_inclusions": violated_inclusions,
            "unknowns": unknowns
        }

    if violated_inclusions:
        return {
            "decision": "DEFER",
            "eligibility": "LIKELY NOT ELIGIBLE",
            "reason": "One or more required inclusion criteria are not satisfied.",
            "unknown_count": len(unknowns),
            "violated_exclusions": violated_exclusions,
            "violated_inclusions": violated_inclusions,
            "unknowns": unknowns
        }

    if len(unknowns) >= 2:
        return {
            "decision": "DEFER",
            "eligibility": "UNCERTAIN",
            "reason": "Too much required information is missing for safe eligibility determination.",
            "unknown_count": len(unknowns),
            "violated_exclusions": violated_exclusions,
            "violated_inclusions": violated_inclusions,
            "unknowns": unknowns
        }

    if len(unknowns) == 1:
        return {
            "decision": "DEFER",
            "eligibility": "POSSIBLY ELIGIBLE",
            "reason": "Patient may be eligible, but one criterion remains unknown.",
            "unknown_count": len(unknowns),
            "violated_exclusions": violated_exclusions,
            "violated_inclusions": violated_inclusions,
            "unknowns": unknowns
        }

    return {
        "decision": "ALLOW",
        "eligibility": "LIKELY ELIGIBLE",
        "reason": "All known inclusion and exclusion criteria are satisfied.",
        "unknown_count": len(unknowns),
        "violated_exclusions": violated_exclusions,
        "violated_inclusions": violated_inclusions,
        "unknowns": unknowns
    }


def baseline_decision(match_results):
    violated = [r for r in match_results if r["status"] == "VIOLATED"]

    if violated:
        return {
            "eligibility": "NOT ELIGIBLE",
            "reason": "At least one criterion is violated."
        }

    return {
        "eligibility": "ELIGIBLE",
        "reason": "No violated criteria detected."
    }