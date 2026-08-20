#26. Represent the friends of two users using sets. Find mutual friends, unique friends, and total unique friends.

user1_friends = {"Alice", "Bob", "Charlie", "David"}
user2_friends = {"Charlie", "David", "Eve", "Frank"}

# Mutual friends
mutual = user1_friends.intersection(user2_friends)
print("Mutual friends:", mutual)

# Friends unique to User 1
unique_user1 = user1_friends.difference(user2_friends)
print("Friends unique to User 1:", unique_user1)

# Friends unique to User 2
unique_user2 = user2_friends.difference(user1_friends)
print("Friends unique to User 2:", unique_user2)

# Total unique friends
total_unique = user1_friends.union(user2_friends)
print("Total unique friends:", total_unique)
