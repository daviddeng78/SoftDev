def sum67(nums):
  track = True
  total = 0
  for n in nums:
    if n == 6:
     track = False
    if track:
      total += n
      continue
    if n == 7:
      track = True
  return total

