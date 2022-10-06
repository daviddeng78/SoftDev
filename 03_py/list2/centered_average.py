def centered_average(nums):
  nums.remove(min(nums))
  nums.remove(max(nums))
  sum = 0
  for x in nums:
    sum += x
  return sum / len(nums)
