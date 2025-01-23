# Paleo Data Hub

This repository contains the files for the Paleo Data Hub website.

## Collections

### Resources

Pages in the resources collection are created by querying the Zenodo API based on
records in _data/zenodo.yml. To add a new resource, add a new entry to that file.
Each entry must include the numeric Zenodo ID and can also include a list of tags.

### Tags

Pages in the tag collection are also generated automatically. Each page in the site 
can be assigned one or more tags using the tags variable in the front matter of the
source file. Currently, the following tags are allowed:

- test

Tags are case sensitive. Invalid tags will raise an error when the build-site.py
script is run.