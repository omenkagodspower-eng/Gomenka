# Largest number in a list
def find_largest(numbers):
    if not numbers:
        return None
    largest = numbers[0]
    for num in numbers:
        if num > largest:
            largest = num 
    return largest 
print(find_largest([3, 41, 56, 21, 76, 9]))
print(find_largest([-10, -5, -2, -18]))
print(find_largest([]))


# Smallest number in list
def find_smallest(numbers):
    if not numbers:
        return none
    smallest = numbers[0] 
    for num in numbers:
        if num < smallest:
            smallest = num
    return smallest 
print(find_smallest([8, 3, 12, 1, 7]))
print(find_smallest([-3, -10, -1, -6]))


# Sum all Numbers
def list_sum(numbers):
    total = 0 
    for num in numbers:
        total += num
    return total
print(list_sum([2, 4, 6, 8]))
print(list_sum([-5, 10, -2]))
print(list_sum([]))


# Count_even Numbers
def Count_even(numbers):
    count = 0
    for num in numbers:
        if num % 2 == 0:
            count += 1
    return count
print(Count_even([1, 2, 3, 4, 6])) 
print(Count_even([1, 3, 5, 7])) 


# Count Occurrences
def count_occurrences(numbers, target):
    watch_count = 0
    for num in numbers:
        if num == target:
            watch_count += 1
    return watch_count
print(count_occurrences([2, 5, 2, 8, 2], target = 2))
print(count_occurrences([1, 4, 7], target = 10))


# Find a Number in a List
def find_number(numbers, target):
    for index, num in enumerate(numbers): 
        if num == target:
           return index
    return -1
print(find_number([10, 25, 30, 45], target := 30))
print(find_number([5, 8, 5, 9], target = 5))
print(find_number([10, 20, 30], target = 99))

# Reverse a list
def reversed_list(items):
    reversed_items = []
    for i in range(len(items) -1, -1, -1):
       reversed_items.append(items[i])

    return reversed_items
print(reversed_list([1, 2, 3, 4]))
print(reversed_list(["a", "b", "c"]))
