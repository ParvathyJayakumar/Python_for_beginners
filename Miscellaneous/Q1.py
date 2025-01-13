#Write a Python function to check if five integers form a circular sequence where the sum of adjacent numbers is even.
def is_circular_even(nums):
    for i in range(len(nums)):
        if (nums[i] + nums[(i + 1) % len(nums)]) % 2 != 0:
            return "NO"
    return "YES"

nums = [int(input("Enter number: ")) for _ in range(5)]
print(is_circular_even(nums))
