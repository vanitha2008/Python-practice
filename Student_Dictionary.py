students = {
    "Vanitha": {
        "department": "BCA",
        "marks": {
            "Python": 85,
            "Java": 78,
            "Maths": 90
        }
    },
    "Anitha": {
        "department": "BCA",
        "marks": {
            "Python": 75,
            "Java": 82,
            "Maths": 80
        }
    }
}

for name, details in students.items():
    total = sum(details["marks"].values())

    print("Student:", name)
    print("Department:", details["department"])
    print("Subject Marks:", details["marks"])
    print("Total Mark:", total)
    print()
