import pathlib
import WrightTools as wt
import numpy as np
import matplotlib.pyplot as plt


here = pathlib.Path(__file__).resolve().parent
data_dir = here.parent / "data"
p = "composed.wt5"
root = wt.open(data_dir / p)


def run(save):
    """import and run all the figure generation stuff in here
    """
    fig, gs = wt.artists.create_figure()

    if save:
        wt.artists.savefig(here / f"{pathlib.Path(__file__).name[:-3]}.png")
    else:
        plt.show()


if __name__ == "__main__":
    from sys import argv
    if len(argv) > 1:
        save = argv[1] != "0"
    else:
        save = True
    run(save)
