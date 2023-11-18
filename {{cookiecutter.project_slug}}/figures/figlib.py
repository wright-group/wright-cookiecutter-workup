import click


command = click.command()

format_argument = click.argument(
    "fmt",
    type=click.Choice(["png", "pdf", "svg"]),
    default="png",
)

interactive_option = click.option(
    "--interactive",
    "-i",
    is_flag=True,
    default=False,
    help="Select for an interactive figure. Format ignored."
)


def composed(*decs):
    def deco(f):
        for dec in reversed(decs):
            f = dec(f)
        return f
    return deco


figure_cli = composed(command, format_argument, interactive_option)
