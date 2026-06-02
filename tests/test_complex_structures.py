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


