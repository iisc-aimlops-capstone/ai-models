def get_disease_diagnosis_prompt() -> str:
    return (
        "Identify the plant disease shown in this leaf. If healthy, state so. "
        "Mention the crop species if identifiable. Also mention the remedies of the disease if identifiable."
    )
