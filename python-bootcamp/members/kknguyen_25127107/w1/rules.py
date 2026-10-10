def can_register_thesis(credits: int, gpa: float) -> bool:
    return credits >= 120 and gpa >= 2.0

def missing(credits,gpa) -> list[str]:
  answer = []
  if credits < 120:
    answer.append(f"Need {120-credits} more credits")
  if gpa < 2.0:
    answer.append(f"Increase GPA by {round(2.0 - gpa,2)}")
  if credits >= 120 and gpa >= 2.0:
    answer.append("Can register thesis")

  return answer

print(can_register_thesis(120, 2.1))
print(missing(118, 1.8))
print(missing(120, 1.8))
print(missing(120, 2.5))