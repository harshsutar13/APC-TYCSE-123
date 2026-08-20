lst = []

for i in range(5):
    n = int(input("Enter number: "))
    lst.append(n)

t = tuple(lst)

print("List:", lst)
print("Tuple:", t)
