from array import array

# Creating an array
arr = array('i', [10, 20, 30, 40, 50])
print("Original array:", arr)

# Accessing elements
print("First element:", arr[0])
print("Third element:", arr[2])

# Updating an element
arr[1] = 25
print("After updating:", arr)

# Adding an element at the end
arr.append(60)
print("After append:", arr)

# Inserting an element
arr.insert(2, 15)
print("After insert:", arr)

# Removing an element
arr.remove(40)
print("After remove:", arr)

# Removing last element
arr.pop()
print("After pop:", arr)

# Finding the index of an element
print("Index of 30:", arr.index(30))

# Counting an element
print("Count of 30:", arr.count(30))

# Reversing the array
arr.reverse()
print("After reverse:", arr)

# Length of array
print("Length of array:", len(arr))