# OSF07: Continuous integration and deployment 

[![Powerpoint Badge](https://img.shields.io/badge/view-deck-blue.svg)](https://storage.googleapis.com/tm-osf/decks/latest/OSF07_Continuous-integration-and-deployment.pdf)

**Difficulty:** :octocat: :octocat: :octocat:

Continuous integration is the process of putting software into production:

- Publishing Python libraries in PyPI
- Compiling and distributing software to your users (`apt-get`, `brew install`)
- Building and serving a website

## Task

- Learn about the continuous integration ecosystem in TM 
- Write a deployment file for an existing open-source/internal project!
- Get **badges** for that project!!

Our **main goal** is to run a continuous integration job in Drone for a TM repo!
If there are no TM repo, you can setup a project in your own Github account! 

* Create a repository `drone-hello-world`
* Write a Python file, `test_hello_world.py` with the following test script:

    ```python
    # test_hello_world.py 
    def test_hello():
        print("Hello world!")

    def test_simple_addition():
        val = 1 + 1
        expected = 2
        assert val == expected
    ```

* Put `pytest` as a dependency for `requirements.txt`

    ```
    # requirements.txt
    pytest
    ```

* Put a `drone.yml` file

    ```yml
    kind: pipeline
    name: test

    steps:
    - name: test
      image: python:3.6-stretch
      commands:
      - pip install -r requirements.txt
      - pytest -v
    ```

* Sign-in to Drone Cloud and commit your files!
