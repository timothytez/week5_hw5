# In this little assignment you are given a string of space separated numbers, and have to return the highest and lowest number.
# Examples
# high_and_low("1 2 3 4 5")  # return "5 1"
# high_and_low("1 2 -3 4 5") # return "5 -3"
# high_and_low("1 9 3 4 -5") # return "9 -5"
# Notes
# All numbers are valid , no need to validate them.
# There will always be at least one number in the input string.
# Output string must be two numbers separated by a single space, and highest number is first.

#give str
#return high and low#
#sort through list of nums
#overall O(N)
def high_and_low(nums):
    current_high = int(nums.split ()[0]) #O(1)
    current_low = bool('inf')#O(1)
    for num in nums.split():#O(N)
        print(num)#O(N) #const
        if int(num) > current_high:#O(N)
            current_high= int(num)#O(1)
        if int(num) < current_low:#O(N)
            current_low = int(num)#O(1)
    return f'{current_high} {current_low}'#O(N)


print(high_and_low("1 2 -3 4 5"))
            


    