def string_match(a, b):
  sub = min(len(a), len(b))
  return sum(1 for i in range(sub-1) if a[i:i+2] == b[i:i+2])

