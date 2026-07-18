nums = [1,4,9,16,25,36,49,64,81,100,36]
idx = 0
x=36
while idx< len(nums):
    if(nums[idx]==x):
        print("Found at = ",idx)
    else:
        print("finding...")
    idx+=1