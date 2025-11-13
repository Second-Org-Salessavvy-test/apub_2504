# Utils Module

This module contains utility functions for common string operations.

## String Utils

### `reverse_string(input_string)`

Reverses a given string.

**Parameters:**
- `input_string` (str): The string to reverse

**Returns:**
- str: The reversed string

**Raises:**
- TypeError: If input is not a string

**Usage:**

```python
from utils import reverse_string

result = reverse_string("hello")
print(result)  # Output: "olleh"
```

**Examples:**

```python
reverse_string("Python")  # Returns: "nohtyP"
reverse_string("hello world")  # Returns: "dlrow olleh"
reverse_string("")  # Returns: ""
```
