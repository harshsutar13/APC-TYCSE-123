#24. Store visitor IDs from two different days in separate sets and determine visitor statistics.

day1_visitors = {101, 102, 103, 104, 105}
day2_visitors = {104, 105, 106, 107, 108}

# Unique visitors across both days
unique_all = day1_visitors.union(day2_visitors)
print("Unique visitors across both days:", unique_all)

# Returning visitors (came on both days)
returning = day1_visitors.intersection(day2_visitors)
print("Returning visitors:", returning)

# Visitors who came only on the first day
only_day1 = day1_visitors.difference(day2_visitors)
print("Visitors who came only on first day:", only_day1)

# Visitors who came only on the second day
only_day2 = day2_visitors.difference(day1_visitors)
print("Visitors who came only on second day:", only_day2)
