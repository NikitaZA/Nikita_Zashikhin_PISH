array = [1, 2, 3, 4, 5]
shift = 2

if len(array) > 0:
    shift = shift % len(array)

rotated_array = array[-shift:] + array[:-shift]

print(rotated_array)