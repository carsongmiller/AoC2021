with open('1_input.txt', 'r') as f:
    nums = [int(i) for i in f.read().splitlines()]

def day1_pt1(nums):
    return sum(b > a for a, b in zip(nums, nums[1:]))

def day1_pt2(nums):
    return sum(nums[i] > nums[i-3] for i in range(3, len(nums)))

print(day1_pt1(nums))
print(day1_pt2(nums))