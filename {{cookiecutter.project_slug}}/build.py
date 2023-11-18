import pathlib
import subprocess
import platform
import click

osf_project = "{{ cookiecutter.osf_id }}"
here = pathlib.Path(__file__).resolve().parent


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


@click.group()
def main():
    pass


@main.command(name="all", help="build all steps")
def all_():
    print('building everything!')
    fetch_data()
    build_data()
    build_figures()
    print_with_line('building done!')


@main.command(name="fetch", help="download and extract the [raw data](https://osf.io/{{ cookiecutter.osf_id }})")
def fetch_data():
    print_with_line('fetch data')
    print_then_call("osf", "-p", osf_project, "clone", str(here / "data"))
    # for name in [...]:
    #     print_then_call("osf", "-p", osf_project, "fetch", f"{name}.wt5", str(here / "data" / f"{name}.wt5"))


@main.command(name="data", help="perform all data processing and simulations")
def build_data():
    print_with_line('workup data')
    print_then_call(python, str(here / "data" / "compose.py"))


@main.command(name="figures", help="generate manuscript figures from the data")
def build_figures():
    print_with_line('figures')
    print_then_call(python, str(here / "figures" / 'fig1.py'))


if __name__ == '__main__':
    main()
