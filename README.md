# deeper_testing
# Section 1 (Basic Assert Methods)


## Task1

Write a test in `src/test.py` to check if the function `to_upper` in `src/text.py` will return the `"ABCDEF"` when called with the argument "abcdef".

## Task2

Write a test in `src/test.py` to check if the function `to_word_list_isupper` in `src/text.py` will return `True` when called with the argument `['I', 'LOVE', 'YOU']`.

## Task3

Write a test in `src/test.py` to check if the function `to_word_list_isupper` in `src/text.py` will return `False` when called with the argument `['i', 'LOVE', 'YOU']`.

# assertRaises

For the following tasks, you need to use `assertRaises`. Python unittest `assertRaises` allows you to verify that a certain exception is raised when your code is run. To use `assertRaises` a context manager is needed.

Example of the usage of a context manager:

```
with open('some_file', 'w') as opened_file:
    opened_file.write('Hola!')
```
Context managers are able to check for specific types of exceptions and prevent them from being raised. This comes in handy when checking for raised exceptions during testing.

For example:
The following test 
```
def test_assert_raises(self)
    with self.assertRaises(KeyError):
        raise KeyError
```
would pass.

On the other hand
```
def test_assert_raises(self)
    with self.assertRaises(KeyError):
        raise IndexError
```
would fail.    


## Task4

Write a test in `src/test.py` to check if the function `to_upper` in `src/text.py` will raise a **TypeError** if called with an argument that is not a string (**str**).

## Task5

Write a test in `src/test.py` to check if the function `to_word_list_isupper` in `src/text.py` will raise a **TypeError** if called with an argument that is not a **list**.

## Task6

Fix both functions **to_upper** and **to_word_list_isupper** in `src/text.py` so they will raise a **TypeError** if the argument was not the right type (**string** in the case of `to_upper` and **list** in the case of `to_word_list_upper`).


## Objectives:
- Learn about assertEqual.
- Learn about assertTrue.
- Learn about assertFalse.
- Learn about assertRaises.

> **Hint:** Run the tests by executing:

    python3 test.py

> Or run the test with more details by executing:

    python3 -m unittest -v test.py


# Section 2 (Unittest Basic 2: More Assert Methods)


## Task 1

Write a test to check if the function `rnd` in `src/app.py` will return the correct value given these arguments: `start = 2` and `end = 20`.

## Task 2

Write a test to check if the function `rnd` in `src/app.py` will not return an out-of-range value given these arguments: `start = 2` and `end = 20`.

## Task 3

What problem is there with testing a method that involves randomized value? Can we be sure that the test passes every time when it has passed once? Add a code comment to the tests of task 1 and 2 about any potential issues with those tests.

## Task 4

Fix the function `max_num_in_list` in `src/app.py`. It should return the highest number of the list of numbers given as the argument. That way it will pass the test.



## Objectives:
- Learn about `assertIn`.
- Learn about **passing** commands.
- Learn about **failing** methods.


> **Hint:** Run the tests by executing:

    python3 test.py

> Or run the test with more details by executing:

    python3 -m unittest -v test.py



# Section 3 (Unittest Mocking)

## Task1

Write a test to check if the `rm` function in `src/app.py` will delete a file.

## Task2

Write a test to check if the `rm` function in `src/app.py` will call the `os.remove` function if the file exists - without deleting the file. Use `unittest.mock` for this purpose.

## Task3

Write a test to make sure that the `rm` function in `src/app.py` will **NOT** call the `os.remove` function if the file **DOES NOT** exist. Use `unittest.mock` for this purpose.

## Task4

Fix the `rm` function in `src/app.py` so that it will raise a **FileNotFoundError** error if the file does not exist.

## Task5

Write a test to check if the `rm` function in `src/app.py` will raise a **FileNotFoundError** error if the file **DOES NOT** exist. Use `unittest.mock` for this purpose.

## Objectives:
- Learn about unittest.mock.
- Learn about mock usage.
- Simulate mock fail cases.

> **Hint:** Run the tests by executing:

    python3 mock_test.py

    python3 no_mock_test.py

> Or run the test with more details by executing:

    python3 -m unittest -v mock_test.py

    python3 -m unittest -v no_mock_test.py
