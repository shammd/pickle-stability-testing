import pickle
import hashlib

def pickle_hash(obj):
    data = pickle.dumps(obj)
    return hashlib.sha256(data).hexdigest()

def roundtrip_check(obj):
    data = pickle.dumps(obj)
    loaded = pickle.loads(data)
    return type(loaded) is type(obj)


float_obj = {
    "value1": 0.1,
    "value2": 0.2,
    "sum": 0.1 + 0.2
}

float_hash1 = pickle_hash(float_obj)
float_hash2 = pickle_hash(float_obj)
print("Floating point values:")
print(float_hash1)
print(float_hash2)
print("Same hash:", float_hash1 == float_hash2)
print("Round-trip type preserved:", roundtrip_check(float_obj))

#NaN value
nan_obj = {
    "value": float("nan")
}

nan_hash1 = pickle_hash(nan_obj)
nan_hash2 = pickle_hash(nan_obj)

print("\nNaN value:")
print(nan_hash1)
print(nan_hash2)
print("Same hash:", nan_hash1 == nan_hash2)
print("Round-trip type preserved:", roundtrip_check(nan_obj))

#Infinity
inf_obj = {
    "value": float("inf")
}
inf_hash1 = pickle_hash(inf_obj)
inf_hash2 = pickle_hash(inf_obj)

print("\nInfinity value:")
print(inf_hash1)
print(inf_hash2)
print("Same hash:", inf_hash1 == inf_hash2)
print("Round-trip type preserved:", roundtrip_check(inf_obj))

#Set
set_obj = {1, 2, 3, 4, 5}

set_hash1 = pickle_hash(set_obj)
set_hash2 = pickle_hash(set_obj)

print("\nSet:")
print(set_hash1)
print(set_hash2)
print("Same hash:", set_hash1 == set_hash2)
print("Round-trip type preserved:", roundtrip_check(set_obj))

#Tuple
tuple_obj = ("Saja", 21, ("course", "testing"))

tuple_hash1 = pickle_hash(tuple_obj)
tuple_hash2 = pickle_hash(tuple_obj)

print("\nTuple:")
print(tuple_hash1)
print(tuple_hash2)
print("Same hash:", tuple_hash1 == tuple_hash2)
print("Round-trip type preserved:", roundtrip_check(tuple_obj))

dict1 = {}
dict1["a"] = 1
dict1["b"] = 2
dict1["c"] = 3

dict2 = {}
dict2["c"] = 3
dict2["b"] = 2
dict2["a"] = 1

dict1_hash = pickle_hash(dict1)
dict2_hash = pickle_hash(dict2)

print("\nDictionary insertion order:")
print(dict1_hash)
print(dict2_hash)
print("Same hash:", dict1_hash == dict2_hash)
print("Round-trip type preserved dict1:", roundtrip_check(dict1))
print("Round-trip type preserved dict2:", roundtrip_check(dict2))