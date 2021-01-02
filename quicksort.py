# 215. Kth Largest Element in an Array
class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        # return sorted(nums)[-k] # builtin
        l, r = 0, len(nums) - 1
        arr_len = len(nums)
        # 第k个最大的元素，即升序排列后，index为len(nums)-k
        k = arr_len - k
        while (l < r):
            print("pivot:", nums[r])
            j = self.partition(nums, l, r)
            print("position:", j)
            print(nums)
            if j == arr_len-k:
                break
            elif j > arr_len-k:
                r = j -1
            else:
                l = j + 1
        return nums[arr_len-k]

    def partition(self, arr, l, r):
        pivot = arr[r]
        i, j = l-1, l  # i keeps track of last item that is less than pivot, j does scanning
        while (j < r):
            if arr[j] < pivot:
                i += 1
                self.swap(arr, i, j)
                print("Swapping:", arr)

            j += 1
        self.swap(arr, r, i + 1)
        return i + 1

    # def partition(self, arr, left, right):
    #     pivot = arr[right]
    #
    #     i = left - 1
    #     for j in range(left, right):
    #         if arr[j] <= pivot:
    #             i += 1
    #
    #             self.swap(arr, i, j)
    #
    #     self.swap(arr, i + 1, right)
    #
    #     return i + 1

    def swap(self, arr, i, j):
        arr[i], arr[j] = arr[j], arr[i]


if __name__ == '__main__':
    quicksort = Solution()

    # input = [3,2,1,5,6,4]
    # k =2
    # print(quicksort.findKthLargest(input,k))


    input = [3,1,2,4]
    k=2
    print(quicksort.findKthLargest(input,k))




