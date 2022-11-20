# nums = [1, 3, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18]

def lucky_num(nums):
    for num in nums:
        if num % 7 == 0:
            return num
    return None
# def lucky_num(nums):
#     return any([num % 7 == 0 for num in nums])


nums = [1, 3, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 21]
lucky = lucky_num(nums)
print(lucky)
