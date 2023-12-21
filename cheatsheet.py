content = """
| Error Name         | Description                                          | Example Program                                       |
| ------------------- | ---------------------------------------------------- | ----------------------------------------------------- |
| SyntaxError         | Syntax error in code.                                | `if x > 5  # Missing colon`                          |
| IndentationError    | Code indentation issues.                             | `def my_function():`\n\treturn 42  # Mixing spaces`   |
| NameError           | Using undefined names.                               | `print(undefined_variable)`                           |
| TypeError           | Operation on wrong type.                             | `result = "42" + 10`                                |
| ValueError          | Correct type, wrong value.                           | `integer_value = int("abc")`                         |
| IndexError          | Invalid sequence index.                              | `my_list = [1, 2, 3]`\n`value = my_list[4]`           |
| KeyError            | Non-existent dictionary key.                         | `my_dict = {"name": "John"}`\n`value = my_dict["age"]` |
| FileNotFoundError   | Manipulating non-existent file.                      | `with open("non_existent_file.txt", "r") as file:`\n`content = file.read()` |
| ZeroDivisionError   | Division by zero.                                    | `result = 10 / 0`                                   |
| AttributeError       | Accessing undefined attribute.                       | `class SomeClass:`\n`\tpass`\n`my_object = SomeClass()`\n`value = my_object.undefined_attribute` |
"""

print(content)
