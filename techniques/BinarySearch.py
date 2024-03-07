# If the target exists, returns its leftmost index.
# Else, returns the index of where it should be.
def binarySearch(nums: list[int], target: int) -> int:
    l, r = 0, len(nums)
    while l < r:
        m = (l + r) // 2
        if nums[m] < target:
            l = m + 1
        else:
            r = m
    return l


nums = [1, 2, 3, 5, 6, 7, 8, 9]

# target exists
# returns the leftmost index

print("nums = " + str(nums))
print("=== target exists ===")
exists = [1, 2, 3, 6, 9]
for i in exists:
    print("index of " + str(i) + " = " + str(binarySearch(nums, i)))

# target does not exist
# returns the index of where the it should be
print("=== target does not exist: index of where it should be ===")
not_exists = [0, -100, 4, 10, 100]
for i in not_exists:
    print("index of " + str(i) + " = " + str(binarySearch(nums, i)))

# verify target exists
print("=== verify target exists ===")
verify = [1, 3, 0, 4, 7, 10]
for i in verify:
    index = binarySearch(nums, i)
    contains = index < len(nums) and i == nums[index]
    print("nums contains " + str(i) + ": " + str(contains))
