# nums=[10,-9,-8,0,0,23,-56,-1000,2,3,8]
# a=[]
# b=[]
# c=[]
# for i in nums:
#     if i<0:
#         a.append(i)
#     elif i==0:
#         b.append(i)
#     else:
#         c.append(i)
# print("отрицательные",a)
# print("нейтральные",b)
# print("положительные",c)


# nums=[10,-9,-8,0,0,23,-56,-1000,2,3,8]
# i=0
# while i<len(nums):
#     if nums[i]<0:
#         nums.pop(i)
#     else:
#         i+=1
# print(nums)

# nums=[0,5,0,3,7,3,0,1,0,9]
# result=[]
# zero_count=nums.count(0)
# for i in nums:
#     if i!=0:
#         result.append(i)
# for j in range(zero_count):
#     result.append(0)
# print(result)

# nums=[0,5,0,3,7,3,0,1,0,9]
# for i in nums:
#     if nums[i]==0:
#         nums.pop(i)
#         nums.append(0)
# print(nums)

# nums=[70,56,89,24,100,60,88]
# nums_copy=nums.copy()
# nums_copy.sort(reverse=True)
# top3=nums_copy[:3]
# print(top3)

# nums=[3,1,5,1,7,8,20,1,2,5,6,7]
# min_val=min(nums)
# while min_val in nums:
#     nums.remove(min_val)
# print(nums)

    



