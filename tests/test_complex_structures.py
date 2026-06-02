import pickle
import hashlib

def pickle_hash(obj):
    data = pickle.dumps(obj)
    return hashlib.sha256(data).hexdigest()
obj = {
    "users": [
        {"name": "Sham", "age": 21},
        {"name": "Hiba", "age": 22}
    ]
}

hash1 = pickle_hash(obj)
hash2 = pickle_hash(obj)

print("Nested structure:")
print(hash1)
print(hash2)
print("Same hash:", hash1 == hash2)

deep_obj = {
    "course": {
        "module": {
            "assignment": {
                "students": [
                    {"name": "Sham", "grade": "A"},
                    {"name": "Hiba", "grade": "B"}
                ]
            }
        }
    }
}

deep_hash1 = pickle_hash(deep_obj)
deep_hash2 = pickle_hash(deep_obj)
print("\nDeep nested structure:")
print(deep_hash1)
print(deep_hash2)
print("Same hash:", deep_hash1 == deep_hash2)

recursive_list = []
recursive_list.append(recursive_list)

recursive_hash1 = pickle_hash(recursive_list)
recursive_hash2 = pickle_hash(recursive_list)
print("\nRecursive list:")
print(recursive_hash1)
print(recursive_hash2)
print("Same hash:", recursive_hash1 == recursive_hash2)

class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age


student = Student("Sham", 21)
student_hash1 = pickle_hash(student)
student_hash2 = pickle_hash(student)

print("\nCustom class object:")
print(student_hash1)
print(student_hash2)
print("Same hash:", student_hash1 == student_hash2)

students = [
    Student("Sham", 21),
    Student("Hiba", 22)
]

students_hash1 = pickle_hash(students)
students_hash2 = pickle_hash(students)
print("\nMultiple objects of same class:")
print(students_hash1)
print(students_hash2)
print("Same hash:", students_hash1 == students_hash2)