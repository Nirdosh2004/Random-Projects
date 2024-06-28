
classRank = {'h': 3, 'a': 29, 'o': 1}


sortedClassRank = dict(sorted(classRank.items(), key=lambda item: item[1]))


for key, value in sortedClassRank.items():
    print(f"{key}: {value}")
