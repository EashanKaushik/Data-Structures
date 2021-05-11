import math
def findMedianSortedArrays(nums1, nums2):


    total_length = len(nums1) + len(nums2)

        
    n1 = 0
    n2 = 0
    median = 0
    count = 0
        
    if total_length % 2 == 0:
            
        index = total_length / 2 
            
        while(count <= index):
                 
            if nums1[n1] <= nums2[n2]:
                    
                count += 1    
                if count == index:
                    return (nums1[n1] + nums2[n2])/2
                n1 += 1

            elif nums1[n1] > nums2[n2]:
                
                count += 1
                if count == index:
                    return (nums1[n1] + nums2[n2]) / 2  
                n2 += 1
    else:

        index = math.ceil(total_length / 2)
        # print(index)
            
        while(count <= index):

            if nums1[n1] <= nums2[n2]:

                count += 1
                if count == index:
                    return nums1[n1]
                n1 += 1

            elif nums1[n1] > nums2[n2]:
                
                count += 1
                if count == index:
                    return nums2[n2]
                n2 += 1
    


print(findMedianSortedArrays([0, 0], [0, 0]))
# print(findMedianSortedArrays([], [1]))