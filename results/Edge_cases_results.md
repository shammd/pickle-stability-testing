**Edge Cases Results**
-Edge Cases Results
-Test Cases
-Floating point values
-NaN value
-Infinity value
-Set object
-Tuple object
-Dictionary insertion order

**Results**
-Most test cases produced identical hashes when the same object was serialized multiple times.
-The dictionary insertion order test produced different hashes. Although the two dictionaries contained the same keys and values, they were created in a different order.
-All round-trip checks passed successfully.

**Analysis**
Floating point values, NaN, Infinity, sets and tuples all produced stable SHA256 hashes during repeated serialization. 
This suggests that pickle handled these data types consistently within the same environment.

The dictionary insertion order test was the most interesting result.
Even though both dictionaries contained the same logical data the generated hashes were different. 
This indicates that pickle preserves insertion order 
when serializing dictionaries which can affect the resulting byte stream and hash value.

-The successful round-trip checks also showed that all tested objects could be serialized and deserialized while preserving their type.

**Conclusion**
For the tested edge cases pickle was deterministic when the same object was serialized repeatedly. 
However dictionary insertion order affected the serialized output
demonstrating that object construction can influence reproducibility even when the stored data is identical.