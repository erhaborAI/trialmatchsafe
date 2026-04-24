def evaluate_match(features, criteria):
    results = []

    for item in criteria["inclusion"]:
        status = "UNKNOWN"
        reason = "Could not determine from patient summary."

        lower = item.lower()

        if "age" in lower:
            if features["age"] is not None:
                status = "SATISFIED" if 18 <= features["age"] <= 75 else "VIOLATED"
                reason = f"Patient age is {features['age']}."

        elif "type 2 diabetes" in lower:
            status = "SATISFIED" if features["type_2_diabetes"] else "VIOLATED"
            reason = "Type 2 diabetes is mentioned." if features["type_2_diabetes"] else "Type 2 diabetes is not mentioned."

        elif "hba1c" in lower:
            if features["hba1c"] is not None:
                status = "SATISFIED" if features["hba1c"] > 7.0 else "VIOLATED"
                reason = f"HbA1c is {features['hba1c']}."

        elif "egfr" in lower:
            if features["egfr"] is not None:
                status = "SATISFIED" if features["egfr"] > 60 else "VIOLATED"
                reason = f"eGFR is {features['egfr']}."

        results.append({
            "type": "Inclusion",
            "criterion": item,
            "status": status,
            "reason": reason
        })

    for item in criteria["exclusion"]:
        status = "UNKNOWN"
        reason = "Could not determine from patient summary."

        lower = item.lower()

        if "stroke" in lower:
            status = "VIOLATED" if features["stroke_history"] else "SATISFIED"
            reason = "Stroke history is present." if features["stroke_history"] else "No stroke history is mentioned."

        elif "trial" in lower:
            status = "VIOLATED" if features["current_trial"] else "SATISFIED"
            reason = "Current trial enrollment is mentioned." if features["current_trial"] else "No current trial enrollment is mentioned."

        elif "egfr less than 45" in lower:
            if features["egfr"] is not None:
                status = "VIOLATED" if features["egfr"] < 45 else "SATISFIED"
                reason = f"eGFR is {features['egfr']}."

        elif "pregnancy" in lower:
            status = "VIOLATED" if features["pregnancy"] else "SATISFIED"
            reason = "Pregnancy is mentioned." if features["pregnancy"] else "Pregnancy is not mentioned."

        results.append({
            "type": "Exclusion",
            "criterion": item,
            "status": status,
            "reason": reason
        })

    return results