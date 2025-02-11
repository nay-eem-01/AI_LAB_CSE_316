students = (
    ("Alex",23,3.56),
    ("Bob",25,3.92),
    ("Eve",19,3.04),
    ("Griffin",21,2.56),
    ("Roy",20,2.93),
)

sortedTuple = tuple(sorted(students,key=lambda x:x[2]))
for s in sortedTuple:
    print(s)