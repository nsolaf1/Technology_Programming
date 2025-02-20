students = [
    {
        "name": "Alice",
        "subjects": ("Math", "Physics", "English"),
        "scores": {"Math": 85, "Physics": 78, "English": 92}},

    {
        "name": "Bob",
        "subjects": ("Math", "Biology", "English"),
        "scores": {"Math": 72, "Biology": 88, "English": 80}},
    {
        "name": "Charlie",
        "subjects": ("Math", "Physics", "Chemistry"),
        "scores": {"Math": 90, "Physics": 95, "Chemistry": 85}},
]


def display_students(students):
    for student in students:
        name = student["name"]
        subjects = ", ".join(student["subjects"])
        print(f"{name} is enrolled in: {subjects}")


display_students(students)
