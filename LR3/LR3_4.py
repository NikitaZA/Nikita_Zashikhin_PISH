def find_max_sum_subarray_simple(array, k):
 
 if k > len(array) or k <= 0:
     return None, 0

 max_sum = -float('inf') 
 result_subarray = []

 
 for i in range(len(array) - k + 1):
    current_subarray = array[i : i + k]
 current_sum = sum(current_subarray)
 
 if current_sum > max_sum:
    max_sum = current_sum
 result_subarray = current_subarray
 
 return result_subarray, max_sum


array = [1, -2, 3, 4, -1, 2, 1, -5, 4]
k = 3


subarray, max_sum = find_max_sum_subarray_simple(array, k)

print(f"Исходный массив: {array}")
print(f"Длина подмассива k: {k}")
print(f"Найденный подмассив: {subarray} (Сумма: {max_sum})")

