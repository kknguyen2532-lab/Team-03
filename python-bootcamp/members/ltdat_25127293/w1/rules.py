def missing(credits: int, gpa: float) -> list[str]:
    """Return a list of human-readable reasons why the student cannot register for the thesis."""
    reasons = []
    
    if credits < 120:
        diff_credits = 120 - credits
        reasons.append(f"need {diff_credits} more credits")
        
    if gpa < 2.0:
        reasons.append("gpa below 2.0")
        
    return reasons