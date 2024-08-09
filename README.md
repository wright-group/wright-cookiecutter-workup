# wright-cookiecutter-workup

A [cookiecutter](https://cookiecutter.readthedocs.io/en/stable/README.html) template for data analysis. 
Includes integration with [Open Science Framework (OSF)](https://osf.io/4znzp/) storage.
Includes a CLI for figure plotting (using [click](https://click.palletsprojects.com/en/)).

# Usage

1. If your are using OSF, start an OSF repository and establish an ID.
    You will want this ID before initializing the project.
    You need not push your data to the OSF repository right away.
2. Install cookiecutter.  
    Using conda:
    ```conda install cookiecutter```
3. Initialize the project folder. 
    Using a terminal in the parent folder for your project destination, run

    ```cookiecutter gh:wright-group/wright-cookiecutter-workup```

    and complete the prompts.
4. The project is now templated. You can begin working up data!  Now is also a good time to start a git repository.


# Notes on osf data storage

* To upload data in bulk (a nested folder structure), use osfclient's upload feature with the recursive setting:
  ```
  osf -u [username] -p [project_id] upload -r [source] [destination]
  ```
  You will need to supply our username password upon request (or you can use token authentications as well).
* The root directory of the remote filesystem is seen as "OSF storage" online; you do not need to include this name when specifying a destination path.
* `build.py fetch` will clone the osf directory into `./data/osfstorage`.  If you alter the contents of the local directory, you can update the remote with the update keyword
  ```
  osf -u [username] -p [project_id] upload -r --update ./path/to/osfstorage .
  ```
* osfclient's upload feature only works for osf-hosted data; you will have to organize remote folders another way if you host data with an add-on service.
