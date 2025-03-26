# Mutable and Immutable in Python

## **Mutable Objects**
Mutable objects **can be changed** after they are created. This means you can modify their content without changing their identity (i.e., memory address).  

### **Examples of Mutable Objects**
- `list`
- `dict`
- `set`
- `bytearray`

### **Example: Mutable List**
```python
lst = [1, 2, 3]
print(id(lst))  # Memory address before modification

lst.append(4)
print(lst)  # [1, 2, 3, 4]
print(id(lst))  # Memory address remains the same
```
✅ The list is modified **without changing its identity**.

---

## **Immutable Objects**
Immutable objects **cannot be changed** after they are created. If you try to modify them, Python creates a new object instead of modifying the existing one.  

### **Examples of Immutable Objects**
- `int`
- `float`
- `tuple`
- `str`
- `frozenset`
- `bytes`

### **Example: Immutable String**
```python
s = "hello"
print(id(s))  # Memory address before modification

s = s + " world"
print(s)  # "hello world"
print(id(s))  # Memory address changes
```
🚫 A new string object is created instead of modifying the original one.

---

## **Key Differences**

| Feature  | Mutable | Immutable |
|----------|---------|-----------|
| Can be changed? | ✅ Yes | 🚫 No |
| Memory address | Remains the same | Changes when modified |
| Examples | `list`, `dict`, `set` | `int`, `str`, `tuple` |

---

### **Conclusion**
- Use **mutable** objects when you need to modify the data in place.
- Use **immutable** objects for fixed values to ensure data integrity and prevent unintended modifications.

Let me know if you need more details! 🚀