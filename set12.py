#12. Create two sets of numbers and find the elements that are present in either set but not in both.

s1 = {1, 2, 3, 4, 5}
s2 = {4, 5, 6, 7, 8}

s3 = s1.symmetric_difference(s2)
print(s3)
