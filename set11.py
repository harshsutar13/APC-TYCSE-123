#11. Create two sets and find elements present in first set but not second, and second set but not first.

s1 = {1, 2, 3, 4, 5}
s2 = {4, 5, 6, 7, 8}

# Elements present in the first set but not the second
s3 = s1.difference(s2)
print("Elements in first set but not second:", s3)

# Elements present in the second set but not the first
s4 = s2.difference(s1)
print("Elements in second set but not first:", s4)
