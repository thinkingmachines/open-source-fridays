#!/usr/bin/env python3

"""Extract features using Geomancer"""

# Import modules
import click
import pandas as pd
from geomancer.spellbook import SpellBook
from geomancer.spells import DistanceToNearest


@click.group()
def main():
    pass


@main.command()
@click.argument("input_path", type=click.Path(exists=True))
@click.argument("output_path", type=click.Path())
@click.option(
    "--spellbook", help="path to SpellBook", type=click.Path(exists=True)
)
def extract_features(input_path, output_path, spellbook):
    """Create new features given a geomancer Spellbook"""

    input_df = pd.read_csv(input_path)
    spellbook = SpellBook.read_json(spellbook)
    output_df = spellbook.cast(input_df)
    output_df.to_csv(output_path, index=False)
    print(output_df)


@main.command()
@click.argument("input_path", type=click.Path(exists=True), nargs=1)
@click.argument("output_path", type=click.Path(), nargs=1)
@click.argument("pois", type=str, nargs=-1)
@click.option(
    "--spellbook-path",
    help="save SpellBook to JSON path",
    type=click.Path(),
    default=None,
)
def get_distance(input_path, output_path, pois, spellbook_path):
    """Get distance given a list of POIs"""
    spells = [
        DistanceToNearest(
            poi,
            feature_name="dist_{}".format(poi),
            dburl="sqlite:///data/source.sqlite",
            source_table="gis_osm_pois_free_1",
        )
        for poi in pois
    ]

    spellbook = SpellBook(spells)
    input_df = pd.read_csv(input_path)
    output_df = spellbook.cast(input_df)
    output_df.to_csv(output_path, index=False)
    print(output_df)

    if spellbook_path:
        spellbook.to_json(spellbook_path)
        print("Saved to {}".format(spellbook_path))


if __name__ == "__main__":
    main()
