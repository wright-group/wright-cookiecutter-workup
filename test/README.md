# test

wright-group boilerplate for working on data and writing a manuscript.

## Instructions for use
1. Clone this repository and make sure you have the package requirements (see `requirements.txt`)
2. Consult `requirements.txt` and install any needed package dependencies
3. Run this script e.g. on Windows:
  ```
  python build.py <args>
  ```
  args [optional]
  - `fetch`: download and extract the [raw data](https://osf.io/j5nws)
  - `data`: perform all data processing and simulations
  - `figures`: generate manuscript figures from the data
  - if no arguments are given, build.py will perform all workflow steps (in order)

