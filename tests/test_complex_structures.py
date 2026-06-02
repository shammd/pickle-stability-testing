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
