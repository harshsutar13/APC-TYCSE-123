#22. Create two sets representing technical skills of two employees and find common, unique, and all skills.

emp1_skills = {"Python", "SQL", "HTML", "CSS", "Git"}
emp2_skills = {"Java", "SQL", "C++", "HTML", "Docker"}

# Common skills
common = emp1_skills.intersection(emp2_skills)
print("Common skills:", common)

# Skills unique to Employee 1
unique_emp1 = emp1_skills.difference(emp2_skills)
print("Skills unique to Employee 1:", unique_emp1)

# Skills unique to Employee 2
unique_emp2 = emp2_skills.difference(emp1_skills)
print("Skills unique to Employee 2:", unique_emp2)

# All available skills
all_skills = emp1_skills.union(emp2_skills)
print("All available skills:", all_skills)
