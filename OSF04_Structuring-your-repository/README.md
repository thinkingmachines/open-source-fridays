# OSF04: Structuring your repository


In this workshop, we will learn about a good open-source repository structure
by creating a simple command-line application. 

The app that we'll build allows us to extract geospatial features given a set
of coordinates. It is based on
[Geomancer](https://github.com/thinkingmachines/geomancer), an open-source tool
we built ourselves!

Our goal looks like this:

```shell
python geogra.py <input> <output> --spellbook=path/to/spellbook.json

```

## Requirements

* geomancer==1.0.1
* pandas
* click

## Set-up

Setup your development environment by running the following commands:

```
make venv
make build
```

Using the `spellbook-bigquery.json` requires access to the BigQuery dataset
`bigquery://tm-geospatial.ph_osm.*`If you don't have access to the
`tm-geospatial` project, then you can use a test SQLite database (only contains
`gis_osm_pois_free_1`, and `gis_osm_roads_free_1` tables):

```shell
wget -O data/source.sqlite --show-progress https://storage.googleapis.com/tm-geomancer/test/source.sqlite
```

