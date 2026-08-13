# 22. Create a dictionary containing numbers from 1 to 20 as keys and their squares as values, but include only even numbers.

even_squares = {i: i ** 2 for i in range(1, 21) if i % 2 == 0}

print("Even numbers (1-20) and their squares:")
print(even_squares)
