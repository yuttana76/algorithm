# =================Linear Search================ #
# Algorithm
def linear_search(nums: list[int], target: int) -> int:
    for i in range(len(nums)):       # (1)
        if nums[i] == target:        # (2)
            return i                 # (3)
    return -1                        # (4)

# --- ทดลองเรียกใช้งาน ---
numbers = [10, 25, 7, 42, 15]
result = linear_search(numbers, 42)
print("เจอที่ตำแหน่ง (index):", result)  # Output: 3

