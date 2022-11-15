# def has_lucky_num(nums):
#     for num in nums:
#         if num % 7 == 0:
#             return True
#     return False

def has_lucky_num(nums):
    return any([num % 7 == 0 for num in nums])


nums = [1, 2, 3, 5, 7, 9, 14, 21]


def has_lucky_num(nums):
    print(nums)
