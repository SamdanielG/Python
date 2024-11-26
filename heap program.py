import heapq

class solution(object):
    def find_kth_largest(self,nums,k):
        """
        :type nums : list [int]
        :type of k : int
        :return value type : int
        """
        h = []
        for num in nums:
            heapq.heappush(h,(-num, num))
            for i in range(k):
              _, largest = heapq.heappop(h)
              if i == k - 1:
                    return largest
arr_nums = [12,14,9,50,61,41]
s=solution()
result = s. find_kth_largest(arr_nums, 1)
print("Third largest element: ",result)
result = s.find_kth_largest(arr_nums, 2)
print("\n second largest element= ",result)
result = s.find_kth_largest(arr_nums, 5)
print("\n Fifth largest element: ",result)