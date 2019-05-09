#!/usr/bin/env python3

"""Extract features using Geomancer"""

# Import modules
import click
import pandas as pd
from geomancer.spellbook import SpellBook


@click.command()
@click.argument("input", type=click.Path(exists=True))
@click.argument("output", type=click.Path())
@click.option(
    "--spellbook", help="path to SpellBook", type=click.Path(exists=True)
)
def extract_features(**opts):
    """Create new features given a geomancer Spellbook"""

    input_df = pd.read_csv(opts["input"])
    spellbook = SpellBook.read_json(opts["spellbook"])
    output_df = spellbook.cast(input_df)
    output_df.to_csv(opts["output"], index=False)


if __name__ == "__main__":
    extract_features()
