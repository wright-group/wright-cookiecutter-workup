import WrightTools as wt
import pathlib


here = pathlib.Path(__file__).resolve().parent


c = wt.Collection(name="root")
# now import and organize the data you want under the root collection



c.save(here / "composed.wt5")
