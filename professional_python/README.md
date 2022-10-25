##Professional Python
These first two programs [palindrome.py](https://github.com/Osvajorge/Data-Science-Platzi-Courses/blob/main/professional_python/palindrome.py) and [isprime.py](https://github.com/Osvajorge/Data-Science-Platzi-Courses/blob/main/professional_python/isprime.py) were created with static typing and with errors in order to check through **mypy** how those errors actually occur.

This is the original error in [palindrome.py](https://github.com/Osvajorge/Data-Science-Platzi-Courses/blob/main/professional_python/palindrome.py)

![Original Error](https://i.imgur.com/5osGsG1.png)

If we run this program with `mypy palindrome.py --check-untyped-defs` instead of `py palindrome.py`

![enter image description here](https://i.imgur.com/vMMG8n2.png)

The same occurs with the isprime.py error.
