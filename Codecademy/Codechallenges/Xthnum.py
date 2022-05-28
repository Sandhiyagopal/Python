def getX(x, nums):
  nums.sort()
  print(nums)
  return(nums[x-1])

print(getX(2, [6, 3, -1, 5]))