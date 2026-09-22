students = (
    ("Vanitha", "BCA"),
    ("Anitha", "BCA", 85),
    ("Keerthi", "BCA", 90, "Python")
)

largest = students[0]

for item in students:
    if len(item) > len(largest):
        largest = item

print("Tuple with more elements:", largest)
print("Number of elements:", len(largest))
