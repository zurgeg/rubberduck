import click

@click.group()
def cli():
    pass

@cli.command()
@click.File("file")
def analyze_document(file):
    # Small wrapper around core.analyze_text
    # English only at the moment.
    text = file.read().split("\n")