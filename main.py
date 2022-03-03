x = input("What was your grade?: ")

def percentage_to_letter(x):
  if x >= 90:
    return "A"
  if 80 <= x < 90:
    return "B"
  if 70 <= x < 80:
    return "C"
  if 60 <= x < 70:
    return "D"
  if x <= 60:
    return "F"

def is_passing(x):
  if x in ["A", "B", "C"]:
    return True
  else:
    return False

print(percentage_to_letter(x))