# Complex Structures Results

## Test Cases

- Nested dictionaries and lists
- Deeply nested structures
- Recursive lists
- Custom class objects
- Multiple objects of the same class

## Results

All complex structure test cases produced identical SHA256 hashes when the same object was serialized multiple times.

All round-trip checks passed. This means that the objects could be serialized and deserialized while preserving their type.

## Analysis

The results suggest that pickle handled the tested complex structures consistently in the same environment. Nested dictionaries, deeply nested structures, recursive lists, and custom class objects all produced stable hashes during repeated serialization.

The recursive list test was especially important because the list contained a reference to itself. Pickle was still able to serialize and deserialize it without errors.

The custom class tests also produced stable hashes, which suggests that pickle preserved the object state consistently for these simple class instances.

## Conclusion

For the tested complex structures, pickle was deterministic within the same environment. No hash differences or round-trip failures were observed in this part of the test suite.