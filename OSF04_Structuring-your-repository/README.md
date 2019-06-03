# OSF04: Structuring your repository

[![Powerpoint Badge](https://img.shields.io/badge/view-powerpoint-orange.svg)](https://docs.google.com/presentation/d/1KscwY9yoPCuN6jKXE2VN2s1tyalssFXJZkHj_ql7r4I/edit?usp=sharing)

**Difficulty:** :octocat: :octocat:

In this workshop, we will learn about a good open-source repository structure
by creating a simple command-line application. By the end of this course,
you'll learn the following:

* Structure an open-source repository
* Create a command-line application using [click](https://github.com/pallets/click)
* Learn how to extract features using [geomancer](https://github.com/thinkingmachines/geomancer)

The app that we'll build allows us to extract geospatial features given a set
of coordinates. It is based on
[Geomancer](https://github.com/thinkingmachines/geomancer), an open-source tool
we built ourselves!


## Task 

Our task is to create a command-line (CLI) application, `geogra.py`, that
allows us to extract geospatial-related features given a set of coordinates. It
involves two subcommands, `extract-features` and `get-distance`.  The slides
will walk through the first one, while the latter is left as an exercise. 

The CLI looks like this:

```shell
python geogra.py extract-features           \
        <input> <output>                    \
        --spellbook=path/to/spellbook.json
```

It is also possible to update `setup.py` to install the command-line app into
your system, allowing us to call the application right away without explicitly
invoking the python interpreter:

```shell
geogra.py extract-features                 \
        <input> <output>                   \
        --spellbook=path/to/spellbook.json
```

## Requirements

Ensure that you have `requirements.in` with the following requirements

* geomancer==1.0.1
* pandas
* click

Then run `make requirements.txt` to generate the full pinned versions of the dependencies.

## Set-up

Setup your development environment by running the following commands:

```shell
make venv
make build
```

You can install this small application by running `python3 setup.py install`

Using the `spellbook-bigquery.json` requires access to the BigQuery dataset
`bigquery://tm-geospatial.ph_osm.*`If you don't have access to the
`tm-geospatial` project, then you can use a test SQLite database (only contains
`gis_osm_pois_free_1`, and `gis_osm_roads_free_1` tables):


```shell
wget -O data/source.sqlite --show-progress https://storage.googleapis.com/tm-geomancer/test/source.sqlite
```


## Usage

You can use the command-line applications implemented here for your needs. If
you want extract features given a SpellBook, then execute the following
command:

```shell
python geogra.py extract-features <input> <output> --spellbook=path/to/spellbook.json
```

To get the distance given a set of POIs

```shell
python geogra.py get-distance                           \
        <input> <output>                                \
        mall supermarket embassy                        \
        --spellbook-path=path/to/output/spellbook.json  \
```
