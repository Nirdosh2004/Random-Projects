
classRank = {'e': 3, 's': 2, 'a': 1}

sorted_classRank = dict(sorted(classRank.items()))

for key, value in sorted_classRank.items():
    print(f"{key}: {value}")


