
def can_register_thesis(credits, gpa):
    return credits >= 120 and gpa >= 2.0


def missing(credits, gpa):
    reasons = []

    if credits < 120:
        reasons.append(f"need {120 - credits} more credits")

    if gpa < 2.0:
        reasons.append(f"need GPA {round(2.0 - gpa, 2)} more")

    return reasons

can_register_thesis(120, 2.0)  # True
can_register_thesis(118, 2.5)  # False
missing(118, 2.5)               # ["need 2 more credits"]
missing(120, 1.8)               # ["need GPA 0.2 more"]