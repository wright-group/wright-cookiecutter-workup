import pathlib
import subprocess
import platform
import click
import requests, zipfile, io
import tomllib


here = pathlib.Path(__file__).resolve().parent
config  = tomllib.load((here / "config.toml").open())
osf_project:str = config["osf"]["id"]
zips:dict = ...

# dict of zipped folders to unpack {osf guid: data subfolder}
# e.g. {"jwfu8": "osfstorage",}
zips = {}

if platform.system() == 'Windows':
    python = 'python'
else:
    python = 'python3'


def print_with_line(s, char='#'):
    s += ' '
    s += char * (80 - len(s))
    print(s)


def print_then_call(*args, **kwargs):
    print_with_line(' '.join(args), '-')
    subprocess.run(args, check=True, **kwargs)


def fetch_data():
    """ download and store data files from OSF"""
    print_with_line('fetch data')
    for guid, subfolder in zips.items():
        print_with_line(f"downloading guid={guid}")
        url = f"https://osf.io/download/{guid}"
        r = requests.get(url, stream=True)
        if r.status_code == 200:
            path = here / "data"
            if subfolder is not None:
                path = path / subfolder
            print_with_line(f"unpacking to {str(path)}")
            z = zipfile.ZipFile(io.BytesIO(r.content))
            z.extractall(path)
        else:
            print("Error downloading file:", r.status_code)


def build_data():
    print_with_line('workup data')
    print_then_call(python, str(here / "data" / "compose.py"))


def build_figures():
    print_with_line('figures')
    print_then_call(python, str(here / "figures" / 'fig1.py'))


@click.group()
def cli():
    pass


@cli.command(name="all", help="build all steps")
def all_():
    print('building everything!')
    fetch_data()
    build_data()
    build_figures()
    print_with_line('building done!')


@cli.command(name="fetch", help="download and extract the [raw data](https://osf.io/{{ cookiecutter.osf_id }})")
def _fetch_data():
    fetch_data()


@cli.command(name="data", help="perform all data processing and simulations")
def _build_data():
    build_data()


@cli.command(name="figures", help="generate manuscript figures from the data")
def _build_figures():
    build_figures()


if __name__ == '__main__':
    cli()
