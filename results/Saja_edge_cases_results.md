**Edge Cases Results**
This part tested floating point values and edge cases to see whether repeated pickle serialization produced identical SHA256 hashes.

# Test cases
TC-06: Floating point values
TC-07: NaN value
TC-08: Infinity value
TC-09: Set object
TC-11: Tuple object
TC-12: Dictionary insertion order

# Results
-Most test cases produced identical hashes when the same object was serialized twice.

-The dictionary insertion order test produced different hashes. This happened because the dictionaries had the same keys and values, but the items were inserted in a different order.

# Conclusion
Pickle was deterministic for repeated serialization of the same object in most edge cases. However, the dictionary insertion order test shows that the exact construction of an object can affect the pickle output.