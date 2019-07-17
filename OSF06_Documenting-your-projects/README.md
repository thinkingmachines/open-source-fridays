# OSF06: Documenting your projects

[![Powerpoint Badge](https://img.shields.io/badge/view-deck-blue.svg)](https://storage.googleapis.com/tm-osf/decks/latest/OSF06_Documenting-your-projects.pdf)

**Difficulty:** :octocat: :octocat: :octocat:

In this workshop, we will learn how to document our Python projects using
[Sphinx](https://sphinx-doc.org)! Sphinx is a powerful tool to create
beautiful, organized, and shareable project documentation with less effort.
In this course, you'll learn the following:

* Writing Python docstrings using the [numpydoc](https://numpydoc.readthedocs.io/en/latest/format.html) format
* Setting-up Sphinx in your code repository
* Basic principles and best practices for writing documentation

## Task

Our task is to create an API documentation for `calculator.py`. It's a simple
app, but it would look better with the right kind of annotation. We will use
the numpydoc format to specify the inputs and expected outputs of each
function.

Afterwards, we will go through the process of setting up a Sphinx `docs`
directory for our project. After setting everything up, we can easily view the
documentation generated in our browser.

### Dependencies

Ensure that you have the following installed inside your system:
- Sphinx>=2.1.0
- sphinx_rtd_theme
- sphinxcontrib-napoleon
