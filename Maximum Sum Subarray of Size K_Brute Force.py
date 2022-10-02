def max_sub_array_of_size_k(k, arr):
    max_sum = 0
    window_sum = 0



    for i in range(len(arr) - k+1):    # 4 OUTER LOOPS:  Len of 6 - 3 = 3... 3 + 1 = 4
        window_sum = 0
        for j in range(i, i+k):        # 3 INNER LOOPS: as k = 3
            window_sum += arr[j]       
        max_sum = max(max_sum, window_sum)
    return max_sum


def main():
    print("Maximum sum of a subarray of size K: " +
          str(max_sub_array_of_size_k(3, [2, 1, 5, 1, 3, 21])))   # should be 25
    print("Maximum sum of a subarray of size K: " +
          str(max_sub_array_of_size_k(2, [2, 3, 4, 1, 5])))      # should be 7


main()