#!/usr/bin/env python3

"""Extract features using Geomancer"""

# Import modules
import click
import pandas as pd
from geomancer.spellbook import SpellBook


@click.command()
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


if __name__ == "__main__":
    extract_features()
