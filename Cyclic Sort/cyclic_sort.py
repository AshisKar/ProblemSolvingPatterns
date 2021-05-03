#Write a function to sort the objects in-place on their creation sequence number in O(n) and without any extra space. 

def cyclic_sort(nums):
  i = 0
  while i < len(nums):
    num_at_i = nums[i] - 1
    if nums[i] != nums[num_at_i]:
      nums[i], nums[num_at_i] = nums[num_at_i], nums[i]  # swap
    else:
      i += 1
  return nums


def main():
  print(cyclic_sort([3, 1, 5, 4, 2]))

main()
