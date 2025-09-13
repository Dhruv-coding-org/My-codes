from collections import Counter

L1 = [1, 2, 2, 3, 2, 3, 4, 5]

# Count frequency of each element
counter = Counter(L1)

# Get the most common element
most_common = counter.most_common(1)[0]  # returns a tuple (element, count)

print(f"Most frequent element is {most_common[0]} (appears {most_common[1]} times)")
