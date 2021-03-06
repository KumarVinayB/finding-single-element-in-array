def singleno(nums):
    return 2*(sum(set(nums)))-sum(nums)



a=[4,1,2,1,2]

print(singleno(a))