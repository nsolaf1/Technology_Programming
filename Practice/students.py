# LIST
# students = ["Elnura", "Korean", 99]
# students = ["Elnura", 99 "Korean"]


# Dictionary 
# key and value
# students = {
#     "name": "Ali",
#     "score": 98,
#     "course": "SFW"
# }
# print(students["course"])
# # print(students["score"] -10)

# students = [
#     {"name": "Liam", "course": "SFW", "score":89, "passed": True},
#     {"name": "ME", "course": "SFW2", "score":90, "passed": False},
#     {"name": "Ali", "course": "SFW3", "score":81, "passed": True},
#     {"name": "Ali1", "course": "SFW3", "score":79, "passed": True}
# ]

# for student in students:
#     if student["passed"] and student["score"] > 80:
#         print(student["score"] + 10)
#         print(student["name"])
        



# sum = 0
# for student in students:
#     sum += student["score"]
# print(sum)
# print(students[1]["name"])
# print("After")
# students[1]["name"] = "Nasirdin"

# for student in students:
#     print(student["name"])

    


studentsList = [
    {"name": "Alice", "subjects": ("Math", "Physics", "English"), "scores": {"Math": 85, "Physics": 78, "English": 92}},
    {"name": "Bob", "subjects": ("Math", "Biology", "English"), "scores": {"Math": 72, "Biology": 88, "English": 80}},
    {"name": "Charlie", "subjects": ("Math", "Physics", "Chemistry"), "scores": {"Math": 90, "Physics": 95, "Chemistry": 85}},
]

def display_students(students):
    for student in students:
        print(f"Name: {student["name"]}")
        print("Subjects: ")
        
        for subject in student["subjects"]:
            print(subject)
        
        print()
        
display_students(studentsList)

