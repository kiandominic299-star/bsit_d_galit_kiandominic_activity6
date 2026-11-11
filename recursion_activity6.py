# ACTIVITY 6: RECURSIVE ARRAY TOOLKIT
# Name: Galit, Kian Dominic D.
# Section: BSIT-2-D

def sum_array(arr):
    if len(arr) == 0:
        
        return 0
    return arr[0] + sum_array(arr[1:])

def find_largest(arr):
    
    if len(arr) == 0:
        raise ValueError("Array must contain at least one number.")

    if len(arr) == 1:
        return arr[0]

    largest_rest = find_largest(arr[1:])

    if arr[0] > largest_rest:
        return arr[0]
    else:
        return largest_rest


def count_number(arr, target):
    
    if len(arr) == 0:
        return 0

    if arr[0] == target:
        return 1 + count_number(arr[1:], target)
    else:
        return count_number(arr[1:], target)


print("=== RECURSIVE ARRAY TOOLKIT ===")

print("\n1. SUM THE ARRAY")
print("Empty array:", sum_array([]))
print("One number:", sum_array([5]))
print("Positive numbers:", sum_array([2, 4, 6]))
print("Positive and negative:", sum_array([10, -5, 3, -2]))

print("\n2. FIND THE LARGEST NUMBER")
print("One number:", find_largest([8]))
print("Largest at beginning:", find_largest([15, 7, 3, 9]))
print("Largest at end:", find_largest([4, 8, 2, 20]))
print("Negative numbers:", find_largest([-8, -3, -12, -5]))

print("\n3. COUNT A CHOSEN NUMBER")
print("Empty array:", count_number([], 5))
print("Target appears several times:",
      count_number([2, 5, 2, 7, 2], 2))
print("Target does not appear:",
      count_number([1, 3, 5, 7], 9))