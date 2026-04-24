import re


def contains_positive(text, positive_terms, negative_terms):
    for neg in negative_terms:
        if neg in text:
            return False

    for pos in positive_terms:
        if pos in text:
            return True

    return False


def extract_patient_features(patient_text):
    text = patient_text.lower()

    age_match = re.search(r"(\d+)[-\s]?year[-\s]?old", text)
    age = int(age_match.group(1)) if age_match else None

    egfr_match = re.search(r"egfr\s*(is|=)?\s*(\d+)", text)
    egfr = int(egfr_match.group(2)) if egfr_match else None

    hba1c_match = re.search(r"hba1c\s*(is|=)?\s*(\d+\.?\d*)", text)
    hba1c = float(hba1c_match.group(2)) if hba1c_match else None

    stroke_history = contains_positive(
        text,
        ["history of stroke", "prior stroke", "stroke history"],
        ["no known history of stroke", "no history of stroke", "stroke history is not documented"]
    )

    pregnancy = contains_positive(
        text,
        ["pregnant", "pregnancy"],
        ["not pregnant", "is not pregnant", "pregnancy is not mentioned"]
    )

    current_trial = contains_positive(
        text,
        ["currently enrolled", "current enrollment", "enrolled in another clinical trial"],
        ["not currently enrolled", "not enrolled", "trial enrollment status is unknown"]
    )

    features = {
        "age": age,
        "egfr": egfr,
        "hba1c": hba1c,
        "type_2_diabetes": "type 2 diabetes" in text or "t2dm" in text,
        "hypertension": "hypertension" in text,
        "prior_mi": "myocardial infarction" in text or "heart attack" in text or "mi" in text,
        "stroke_history": stroke_history,
        "pregnancy": pregnancy,
        "current_trial": current_trial
    }

    return features