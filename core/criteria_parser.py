def parse_criteria(trial_text):
    lines = trial_text.splitlines()

    inclusion = []
    exclusion = []
    current_section = None

    for line in lines:
        clean = line.strip()

        if not clean:
            continue

        lower = clean.lower()

        if "inclusion" in lower:
            current_section = "inclusion"
            continue

        if "exclusion" in lower:
            current_section = "exclusion"
            continue

        clean = clean.replace("-", "").strip()

        if current_section == "inclusion":
            inclusion.append(clean)

        elif current_section == "exclusion":
            exclusion.append(clean)

    return {
        "inclusion": inclusion,
        "exclusion": exclusion
    }