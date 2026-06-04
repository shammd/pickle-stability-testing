#This is the Python Version Test
import pickle
import hashlib
import sys

def pickle_hash(obj):
    data = pickle.dumps(obj)
    return hashlib.sha256(data).hexdigest()

#Test Case:Checks if same object produces identical hashes in the current Python version
test_obj = {
    "user": "Hiba",
    "numbers": [1, 2, 3],
    "active": True
}

# Compare pickle output across Python versions
# Serialize the same object twice and compare hashes
# SHA256 is used to verify whether the pickle output is identical

hash1 = pickle_hash(test_obj)
hash2 = pickle_hash(test_obj)
print("Python version:", sys.version)
print("Test object:")
print(hash1)
print(hash2)
print("Same hash:", hash1 == hash2)