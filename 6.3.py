nums = int(input("Enter nums:"))

while nums > 9:
    result = 1
    for i in str(nums):
        result *= int(i)

    nums = result

print(nums)
