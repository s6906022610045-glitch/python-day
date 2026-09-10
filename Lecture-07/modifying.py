student = {"name": "Alice", "age": 25, "grage": "A"}

student["age"] = 26
student["major"] = "Computer Science"
print(student)

del student["grage"]
print(student)

remove_major = student.pop("major")
print(remove_major)
print(student)
