# OSF05: Writing tests and modularizing your code

In this workshop, we will learn about the importance of testing your code to
ensure that there are no bugs or unexpected errors when running them. By the
end of this course, you'll learn the following:

* Modularizing your code so that they become "test-friendly"
* Difference between unit tests and integration tests
* Writing and running tests in Python using the [pytest](https://docs.pytest.org/en/latest/) framework
* Program robustness via code coverage (not always the case!)

For today, we'll train a very simple machine learning model on a toy image
dataset (MNIST). Testing on ML is pretty challenging, since the latter involves
a large amount of uncertainty.

## Task

There are two tasks for this activity, first we need to refactor a pipeline
code, and then write tests for the refactored pipeline.

### Modularizing code

Our task is to refactor a simple MNIST classification pipeline found in
`pipeline-problem.py`. We need to create two files:

* `pipeline.py`: that will contain all our solutions for `pipeline-problem.py`, and
* `src.py`: that will contain all necessary functions to solve the problem.

### Writing tests

The next step is to write tests for the refactored pipeline. We will create two
sets of test suites: one for unit testing (`test_src.py`) and another
integration testing (`test_pipeline.py`). To execute the tests, simply run:

```shell
pytest -v
```

Ensure that all test cases will pass. You can also try checking for test
coverage by installing `pytest-cov` and running:

```shell
pytest --cov=. -v
```


## Requirements

Ensure that you have the following installed:

* click
* scikit-learn
* numpy
* pytest
* pytest-cov (optional)


