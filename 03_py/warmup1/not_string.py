def not_string(str):
  if str[:3] == "not":
    return str
  return "not " + str
Given a string, return a new string where "not " has been added to the front. However, if the string already begins with "not", return the string unchanged.


print(not_string('candy')) #→ 'not candy'
print(not_string('x')) #→ 'not x'
print(not_string('not bad')) #→ 'not bad'