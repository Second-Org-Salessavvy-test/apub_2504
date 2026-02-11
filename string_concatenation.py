# String Concatenation Examples in Python

# Method 1: Using + operator
first_name = "John"
last_name = "Doe"
full_name = first_name + " " + last_name
print("Method 1 (+ operator):", full_name)

# Method 2: Using f-strings (Python 3.6+)
full_name = f"{first_name} {last_name}"
print("Method 2 (f-strings):", full_name)

# Method 3: Using format() method
full_name = "{} {}".format(first_name, last_name)
print("Method 3 (format()):", full_name)

# Method 4: Using join()
words = ["Hello", "World", "from", "Python"]
sentence = " ".join(words)
print("Method 4 (join()):", sentence)

# Method 5: Using % operator
full_name = "%s %s" % (first_name, last_name)
print("Method 5 (% operator):", full_name)

# Method 6: Multiple concatenations
greeting = "Hello, " + "my name is " + first_name + " " + last_name + "!"
print("Method 6 (multiple +):", greeting)
