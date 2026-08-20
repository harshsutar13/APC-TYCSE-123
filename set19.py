#19. Create two sets: morning session and afternoon session. Find various student combinations.

morning = {"Aryan", "Balraj", "Charan", "Dhanush"}
afternoon = {"Charan", "Dhanush", "Emran", "Fukra"}

# Students present in both sessions
both = morning.intersection(afternoon)
print("Students present in both sessions:", both)

# Students present only in the morning
only_morning = morning.difference(afternoon)
print("Students present only in morning:", only_morning)

# Students present only in the afternoon
only_afternoon = afternoon.difference(morning)
print("Students present only in afternoon:", only_afternoon)

# Students present in at least one session
at_least_one = morning.union(afternoon)
print("Students present in at least one session:", at_least_one)
