def square_and_sort(arr):
    n = len(arr)
    result = [0] * n
    left, right = 0, n - 1
    index = n - 1
    
    while left <= right:
        if abs(arr[left]) > abs(arr[right]):
            result[index] = arr[left] ** 2
            left += 1
        else:
            result[index] = arr[right] ** 2
            right -= 1
        index -= 1
    
    return result

arr = [-12, -8, -7, -5, 2, 4, 5, 11, 15]
print(square_and_sort(arr))
