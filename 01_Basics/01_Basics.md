# 01_Basics

- ### File Naming Convention
  * Lowercase with underscores: This is the standard convention for Python file names.

    Example: 
    > my_module.py, utils.py

  * Descriptive names: The file name should reflect the contents of the file.

  * Avoid special characters: Use only letters, numbers, and underscores.

  * Consistent naming: Maintain a consistent naming style throughout your project.

- Create a file `hello_python.py`

``` 
print('Hello Python')
```
- To execute the file `hello_python.py`
> python ./hello_python

Output:
```
Hello Python
```

---

- create a function in the file `hello_python.py`

```
print('Hello Python')

def hello(n):
    print(n)

hello("Pikachu")

```

- To execute the file `hello_python.py`
> python ./hello_python

Output:
```
Hello Python
Pikachu

```
---
### Import a function into a different file

- create another file `greet.py`

```python
from hello_python import hello

hello('master')

```

- To execute the file `greet.py`
> python ./greet.py

```
Hello Python
Pikachu
master

```
***
### Automatically while execution of the file `greet.py`a new folder `__pycache__` is created with a file `hello_python.cpython-312.pyc`