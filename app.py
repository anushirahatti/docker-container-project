#!/usr/bin/env python
import click
from datetime import date

@click.command()
def hello():
    today = date.today()
    format = today.strftime("%b-%d-%Y")
    click.echo('Hello Aniruddha!')
    print('Today is:', format)

if __name__ == '__main__':
    hello()