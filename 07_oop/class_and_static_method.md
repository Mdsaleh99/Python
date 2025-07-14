# Understanding `@classmethod` and `@staticmethod` in Python

Python provides two important decorators for methods inside classes: `@classmethod` and `@staticmethod`. Both are used to define methods that are not regular instance methods, but they serve different purposes.

---

## 1. `@classmethod`

### What is a Class Method?

- A class method receives the class (`cls`) as its first argument, not the instance (`self`).
- It can access and modify class state that applies across all instances of the class.
- It is defined using the `@classmethod` decorator.

### When to Use?

- When you need to create factory methods that can create class instances in different ways.
- When you want to operate on the class itself, not on a specific instance.

### Example

```python
class ChaiOrder:
    def __init__(self, tea_type, sweetness, size):
        self.tea_type = tea_type
        self.sweetness = sweetness
        self.size = size

    @classmethod
    def from_dict(cls, order_data):
        return cls(
            order_data["tea_type"],
            order_data["sweetness"],
            order_data["size"],
        )

    @classmethod
    def from_string(cls, order_string):
        tea_type, sweetness, size = order_string.split("-")
        return cls(tea_type, sweetness, size)
```

**Usage:**

```python
order1 = ChaiOrder.from_dict({"tea_type": "masala", "sweetness": "medium", "size": "Large"})
order2 = ChaiOrder.from_string("Ginger-Low-Small")
```

Here, `from_dict` and `from_string` are alternative constructors for the `ChaiOrder` class.

---

## 2. `@staticmethod`

### What is a Static Method?

- A static method does **not** receive an implicit first argument (neither `self` nor `cls`).
- It behaves like a plain function, but belongs to the class's namespace.
- It is defined using the `@staticmethod` decorator.

### When to Use?

- When you want to group a utility function with a class, but it does not need to access or modify the class or instance.
- For helper functions related to the class.

### Example

```python
class ChaiUtils:
    @staticmethod
    def is_valid_size(size):
        return size in ["Small", "Medium", "Large"]
```

**Usage:**

```python
print(ChaiUtils.is_valid_size("Medium"))  # True
```

---

## Key Differences

| Feature           | `@classmethod`                  | `@staticmethod`                |
|-------------------|---------------------------------|-------------------------------|
| First Argument    | `cls` (the class itself)        | None                          |
| Access to Class?  | Yes                             | No                            |
| Access to Instance? | No                            | No                            |
| Use Case          | Alternative constructors, class-level operations | Utility/helper functions      |

---

## Summary

- Use `@classmethod` when you need to access or modify the class state or provide alternative constructors.
- Use `@staticmethod` for utility functions that belong to the class logically but do not need to access class or instance data.