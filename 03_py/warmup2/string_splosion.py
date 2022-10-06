def string_splosion(str):
  s = ""
  index = 0
  for i in str:
    s += str[:index +1]
    index += 1
  return s
