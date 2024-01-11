# 0x00. Python - Variable Annotations
# Concepts 📔
_For this project, we expect you to look at this concept:_

* [Advanced Python](https://intranet.alxswe.com/concepts/554)

# 1. Advanced Python
Python is a dynamically-typed language. That means that variable types are dynamically set at run-time, upon assignment of a value to a variable.

For example, in
```groovy
def fn(a, b):
    return a + b
```
The types of `a` and `b` are not known at build-time, only when `a` and `b` are assigned values at run-time.

Hence, calling
```groovy
fn("a", 1)
```
somewhere in your code will not raise an exception until the code is actually executed and the function is called:
```groovy
>>> fn("a", 1)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: can only concatenate str (not "int") to str
```
In Python 3, type annotations do not change this. Python is still a dynamically-typed language. Type annotations serve the following purpose:

* **Code documentation**: thanks to them, a developer reading type-annotated code (his own or someone else’s) will know exactly what type each variables is supposed to be. This helps reduce bugs and exceptions and accelerate the development cycle.
* **Linting and validation**: code editors and continuous integration (CI) pipelines can be configured to automatically validate type-annotated code at build-time and catch bugs before they make it to production.
---

![y9y25tefi5401](https://github.com/elyse502/alx-backend-python/assets/125453474/abb4d701-d9f3-4b57-97cc-11b2a0d2f2f7)

# Resources🏗️
### Read or watch:
* [Python 3 typing documentation](https://docs.python.org/3/library/typing.html)
* [MyPy cheat sheet](https://mypy.readthedocs.io/en/latest/cheat_sheet_py3.html)

# Learning Objectives 📖
At the end of this project, you are expected to be able to [explain to anyone](https://fs.blog/feynman-learning-technique/), **without the help of Google**:

* Type annotations in Python 3
* How you can use type annotations to specify function signatures and variable types
* Duck typing
* How to validate your code with `mypy`

# Requirements 🏛️
## General🧵
* Allowed editors: `vi`, `vim`, `emacs`
* All your files will be interpreted/compiled on Ubuntu 18.04 LTS using `python3` (version 3.7)
* All your files should end with a new line
* The first line of all your files should be exactly `#!/usr/bin/env python3`
* A `README.md` file, at the root of the folder of the project, is mandatory
* Your code should use the `pycodestyle` style (version 2.5.)
* All your files must be executable
* The length of your files will be tested using `wc`
* All your modules should have a documentation (`python3 -c 'print(__import__("my_module").__doc__)'`)
* All your classes should have a documentation (`python3 -c 'print(__import__("my_module").MyClass.__doc__)'`)
* All your functions (inside and outside a class) should have a documentation (`python3 -c 'print(__import__("my_module").my_function.__doc__)'` and `python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)'`)
* A documentation is not a simple word, it’s a real sentence explaining what’s the purpose of the module, class or method (the length of it will be verified)























































































