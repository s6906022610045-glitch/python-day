survey_results = [
    ["Python", "JavaScript", "C++"],
    ["Python", "JavaScript", "C#"],
    ["Python", "Java"],
    ["Python", "C++", "JavaScript"],
    ["Python", "JavaScript", "C++", "Java"]
]

# Convert list to set
sets = [set(x) for x in survey_results]

# 1. Chosen by all participants
result = sets[0]
for s in sets[1:]:
    result = result & s
print("1.", result)

# Count languages
count = {}

for participant in survey_results:
    for language in participant:
        if language in count:
            count[language] += 1
        else:
            count[language] = 1

# 2. Chosen by one participant
result = {lang for lang, num in count.items() if num == 1}
print("2.", result)

# 3. Number of unique languages
all_languages = set()
for participant in survey_results:
    all_languages.update(participant)

print("3.", len(all_languages))

# 4. Chosen by exactly two participants
result = {lang for lang, num in count.items() if num == 2}
print("4.", result)

# 5. Participants with exactly the same set
same = []

for i in range(len(sets)):
    for j in range(i + 1, len(sets)):
        if sets[i] == sets[j]:
            same.append([i + 1, j + 1])

print("5.", same)