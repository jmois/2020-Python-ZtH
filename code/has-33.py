def has_33(nums):
    for i in range(0,len(nums) -1):
        if nums[i] == 3 and nums[i + 1] == 3:
            x = True
        else:
            x = False
    print(x)

if __name__ == '__main__':
    has_33([1, 2, 3, 3])
    has_33([1, 3, 1])