import click

from proj.app import create_app
from proj.models import db


@click.group()
def cli():
    pass


@cli.command()
def initdb():
    with create_app().app_context() as ctx:
        db.create_all()
    click.echo('Initialized the database')


@cli.command()
def dropdb():
    with create_app().app_context() as ctx:
        db.drop_all()
    click.echo('Dropped the database')


if __name__ == '__main__':
    cli()
