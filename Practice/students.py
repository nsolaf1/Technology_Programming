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

# def display_students(students):
#     for student in students:
#         print(f"Name: {student["name"]}")
#         print("Subjects: ")
        
#         for subject in student["subjects"]:
#             print(subject)
        
#         print()
        
# display_students(studentsList)



library_books = {
    "B001": {"title": "Основы Python", "borrower": "Алиса", "due_date": -5, "fine_rate": 0.50},
    "B002": {"title": "Наука о данных", "borrower": "Боб", "due_date": 3, "fine_rate": 0.75},
    "B003": {"title": "Введение в ИИ", "borrower": None, "due_date": 0, "fine_rate": 0.25},
    "B004": {"title": "Алгоритмы", "borrower": "Алиса", "due_date": 2, "fine_rate": 1.00}
}

def borrowed_booked(books):
    __init__ 
    for book in books.values():
        print(book['title'])
        # if book["borrower"] and book["due_date"] < 0:
        #     print(book["borrower"])
            
        
    

borrowed_booked(library_books)


