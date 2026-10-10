credits=int(input("Your credits: "))
gpa=float(input("Your gpa: "))
def can_register_thesis(credits:int,gpa:float)->bool:
    return credits>=120 and gpa>=2.0 
def missing(credits,gpa)->list[str]:
    reason=[]
    if credits < 120:
        reason.append(f"need {120 - credits} more credits")
    if gpa < 2.0:
        reason.append("GPA must be at least 2.0")
    return reason
print(can_register_thesis(credits,gpa))
print(missing(credits,gpa))