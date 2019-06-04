---
theme: metropolis
title: Open Source Fridays
subtitle: Structuring your repository 
date: May 10, 2019
aspectratio: 169
institute: 'Thinking Machines Data Science'
---


# Introduction

In open-source, adhering to a **repository structure** is helpful:

* Organizes your code into logical parts
* Enables other contributors to easily navigate throughout your codebase
* Most repository structures are standardized, from years of best practices 

---

For now, we'll focus on Python projects. This can be helpful if:

* You are interested in starting or contributing to an open-source project
* Want to help clean-up some scripts in your client projects
* Just wanna learn new things (*totally awesome*)!

# Learning Goals

For today, we'll learn the following:

- Structuring an open-source repository (or any Python project)
- Create a command-line application using `click`
- Learn how to extract features using `geomancer`

# Brief intro to geomancer

We'll extract geospatial features using our own open-source tool: Geomancer!

![](geomancer-header.png)

It allows us to obtain geospatial features (called **Spells**) such as "distance to nearest
mall" or "number of supermarkets" given a set of coordinates.

---

You can export the Spells into a JSON file called **SpellBook** in order to
share your features to others!

![Spellbook workflow](spellbook_workflow.png)


---


:::::::::::::: {.columns}
::: {.column width="50%"}

How Spellbooks are created:

- First we define the spells we want to save into the Spellbook
- Then we put those spells in a `list`, and use that to instantiate a `SpellBook`
- Lastly, you can save the `SpellBook` into a JSON file by  calling the `to_json(filename : str)` method

:::
::: {.column width="50%"}


\tiny
```python
from geomancer.spells import DistanceToNearest
from geomancer.spellbook import SpellBook

spellbook = SpellBook([
# Get distance to nearest supermarket
DistanceToNearest(
    "supermarket",
    source_table="ph_osm.gis_osm_pois_free_1",
    feature_name="dist_supermarket",
    dburl="bigquery://tm-geospatial"
),
# Get distance to nearest embassy
DistanceToNearest(
    "embassy",
    source_table="ph_osm.gism_osm_pois_free_1",
    feature_name="dist_embassy",
    dburl="bigquery://tm-geospatial"
)
])

spellbook.to_json("my_features.json")
```
:::
::::::::::::::


# Task # 1: Setup your dependencies

In Thinking Machines, we often manage our dependencies using a `Makefile` (think
of an automated chef that cooks according to a recipe):

```shell
make [RECIPE]
$ make venv
```
---

The recipes (or **build targets**) is simply a list of steps that are executed
when the `make` command is called:

```bash
# Makefile
venv: 
    python3 -m venv venv            
    venv/bin/pip3 install pip-tools  
```

So whenever we run `make venv`, two things happen:

* A virtual environment called `venv` is created, and
* The package `pip-tools` is installed in that `venv`

---

## Instructions

1. In your project root, **create a `Makefile`**, and copy our
   standard Python Makefile in [this
   link](https://github.com/thinkingmachines/gists/blob/master/python/Makefile) (*feel free to explore what's inside!*):

```
github.com/thinkingmachines/gists/blob/master/python/Makefile
```

2. **Create a `requirements.in`** file and declare the following as dependencies:

    ```shell
    geomancer==1.1.0
    click
    pandas
    ```

3. Then **execute the following**:

    ```shell
    $ make venv
    $ make build
    ```


# Tasks # 2 and # 3: Building the command-line application 


:::::::::::::: {.columns}
::: {.column width="40%"}

Do you remember `git`?

* You have the application name: `git`
* Then a subcommand: `add`, `commit`, `push`
* You also have arguments: `origin`, `master`
* And options/flags: `--message`

:::
::: {.column width="60%"}

## Git in action

```shell
git status
git add file.txt
git commit --message "Add file.txt"
git push origin master
```


## Common abstraction:

```shell
APPNAME VERB NOUN --ADJECTIVE
APPNAME COMMAND ARG --OPTION
```

:::
::::::::::::::

---

## Advantages of a command-line application

* Less overhead when setting-up
* Can easily be shared to others
* Sometimes, less overhead with respect to memory

---

## Goal

```shell
$ python geogra.py                      \
     coordinates.csv output.csv         \
     --spellbook=path/to/spellbook.json 
```

## Specifications

- It should take a set of coordinates, extract features given a SpellBook, then
save the output as a CSV file
    + 1 command: `geogra.py` [root]
    + 2 options: `input csv`, `output csv`
    + 1 flag: `--spellbook`



# Task # 2: Writing the business logic 

## Instructions

* Write the business logic first.
    + Input: a set of coordinates in CSV, SpellBook
    + Output: filepath for output CSV
* Create a file called `geogra.py`, and make a function called
    `extract(input_path, output_path, spellbook)`

1. Using `pandas`, read the input CSV file into a DataFrame
2. Using `geomancer`, read the SpellBook JSON file 
3. Using `geomancer`, cast a spell on the DataFrame to produce another
   DataFrame
4. Using `pandas`, save the resulting DataFrame to the `output_path`

---

## Hints

- If you are not sure on how to do something, then read the API documentation:
    + Geomancer, [geomancer.readthedocs.io](geomancer.readthedocs.io)
    + Pandas, [pandas.pydata.org/pandas-docs/stable/](https://pandas.pydata.org/pandas-docs/stable/)
- You can read SpellBooks using `spellbook.read_json(path/to/spellbook.json)`
- You can save to CSV in pandas using `to_csv(path/to/output.csv)` method

# Task # 3: Turning business logic into a command-line app 

## Instructions

To convert a function into a command-line application, we'll use a
framework called Click!

- To turn your function into a **command**, simply add the `@click.command()`
    decorator.
- If you want to add an **argument**, just add another decorator:
    `@click.argument("parameter_name")`
- If you want to add an option/flag, add another decorator
    `@click.option("--flag", help="help message")`

You can find more at
[click.palletsprojects.com/en/7.x/options/](https://click.palletsprojects.com/en/7.x/options/)

---

## Sample

\small 
```python
import click

@click.command()
@click.argument("name", type=str)
@click.option("--loud", help="Add exclamation point", type=bool)
def greet(name, loud):
    msg = "Greetings, General {}"
    if loud:
        print(msg.format(name) + "!")
    else:
        print(msg.format(name))

if __name__ == "__main__":
    greet()
```

---

## Check if it's working

1. See if the command-line app checks out:

    ```shell
    $ python geogra.py --help
    ```

2. Test if the business logic executes well
    + Download `coordinates.csv` for some sample coordinates
    + Download `spellbook-bq.json` for your spellbook
    + Run your program!

*(For our next sessions, we'll teach you a more formal way of testing your
code)*

# Basic packaging 

:::::::::::::: {.columns}
::: {.column width="40%"}

To turn our application into an installable package, we need to create a
`setup.py`:

- Allows us to upload our package to a PyPI server (a la `pip install geogra.py`)
- We can also install our package system-wide or inside our `venv`:
    + `python setup.py install`

:::
::: {.column width="60%"}

\small
```python
from setuptools import find_packages, setup

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name="geogra.py",
    version="1.0.0",
    install_requires=requirements,
    scripts=["geogra.py"]
)
```

:::
::::::::::::::


# Challenge

## Additional Task

Create a subcommand, `get-distance` that takes:

- A set of coordinates in a CSV file
- Output CSV file path
- Multiple string arguments for POIs: e.g., mall, supermarket, embassy, etc.

And outputs:

- A CSV file with the distance-to-nearesat to all those points

---

## This will print and output the resulting dataframe

```shell
$ python geogra.py get-distance   \
    coordinates.csv output.csv    \
    mall supermarket embassy
```

## This will save resulting spell into a SpellBook

```shell
$ python geogra.py get-distance  \
    coordinates.csv output.csv   \
    mall supermarket embassy     \
    --spellbook-path=path/to/output/spellbook.json
```

--- 

Given a POI, you can create a spell for getting the distance-to-nearest:

\small 
```python
from geomancer.spells import DistanceToNearest

# Using BigQuery
spell = DistanceToNearest(poi, # a string
         feature_name="dist_{}".format(poi),
         dburl="bigquery://tm-geospatial",
         source_table="tm-geospatial.ph_osm.gis_osm_pois_free_1"
)

# Using SQLite
spell = DistanceToNearest(poi, # a string
        feature_name="dist_{}".format(poi),
        dburl="sqlite:///data/source.sqlite",
        source_table="gis_osm_pois_free_1"
)
```

# Final Notes

- Today, we've learned the following:
   + Declaring dependencies in a `Makefile`
   + Writing business logic as a Python method
   + Turning business logic into reusable command-line applications
- We've also learned how to use three new tools:
   + Click, for creating command line apps
   + Geomancer, our tool for geospatial feature engineering
   + setup.py, for building python packages
