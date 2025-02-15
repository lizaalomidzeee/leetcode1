class Solution(object):
    def intersection(self, nums1, nums2):
        return list(set(nums1)) & set(nums2)
    
solution = Solution()
print(solution.intersection([1,2,2,1], [2,2]))

# set გარდაქმნის ყველა ობიექტს უნიკალურად რის შემდგომაც &-ამ ოპერაციით ვეძებთ ერთნაირ ობიექტებს და პასუხი გამოგვაქვს ლისტად.