nums = [1,4,9,16,25,36,49,64,81,100,36]
print(nums)
x = int(input("Enter element to search from list= "))
i = 0
for val in nums:
    if(nums[i]== x):
        print("Found at ",i)  
    i+=1