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
        "scores": {"Math": 90, "Physics": 95, "Chemistry": 85, "IT": 45}},
]


def display_students(students):
    for student in students:
        name = student["name"]
        subjects = ", ".join(student["subjects"])
        print(f"{name} is enrolled in: {subjects}")


# display_students(students)


def get_average_score(name, students):
    for student in students:
        if student["name"] == name:
            scores = student["scores"].values()
            return sum(scores) / len(scores)

# print(get_average_score("Charlie", students))

def find_top_student(students):
    top_score = 0
    top_student = []
    for student in students:
        avg_score = sum(student["scores"].values())/(len(student["scores"]))
        
        if avg_score > top_score:
            top_score = avg_score
            top_student = student["name"]
    return top_student

print(find_top_student(students))

            



