# Q1. Write a Python program to find the maximum and minimum sum of a subarray in a given list of integers. A subarray is a contiguous part of an array.
# Solution ==>


ori_list   = [0,1,-1,0,-1,0,-1,0,-1]
sub_array  = []
subset     = []
subset_sum = []
i = 0
j = 0
while j < len(ori_list):
    i = j
    sum = 0
    while i < len(ori_list):
        sum += ori_list[i]
        subset.append(ori_list[i])
        sub_array.append(subset.copy())
        subset_sum.append(sum)
        i +=1
    subset.clear()
    i =0
    j +=1
print(sub_array)
print(subset_sum)
subset_sum.sort()
print(f"The Max and Minimum of Sum of Subarray will be respectively. : {subset_sum[-1]} , {subset_sum[0]} ")

