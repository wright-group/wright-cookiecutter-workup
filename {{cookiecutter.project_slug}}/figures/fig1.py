import pathlib
import WrightTools as wt
import matplotlib.pyplot as plt

from figlib import figure_cli


here = pathlib.Path(__file__).resolve().parent
data_dir = here.parent / "data"


@figure_cli
def main(fmt, interactive=False):
    """create your figure here!
    """

    p = "composed.wt5"
    root = wt.open(data_dir / p)

    fig, gs = wt.artists.create_figure()
    ax = fig.add_subplot(gs[0])

    if interactive:
        plt.show()
    elif fmt in ["png", "pdf", "svg"]:
        wt.artists.savefig(here / f"{pathlib.Path(__file__).name[:-3]}.{fmt}")


if __name__ == "__main__":
    main()
