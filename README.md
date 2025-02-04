# Paleo Data Hub

This repository contains the files for the Paleo Data Hub website.

## Site structure

The site is organized primarily by collections. The following

### Community

### Paleo data ecosystem

### Browse by topic

#### Explanation

#### How to guides

#### Tutorials

### Resources

Items in the resources collection are created by querying the Zenodo API based on
records in _data/zenodo.yml. To add a new resource, add a new entry to that file.
Each entry must include a numeric Zenodo ID and can also include a list of tags.

### Tags

Pages in the tag collection are also generated automatically. Each page in the site 
can be assigned one or more tags using the tags variable in the front matter of the
source file. Tags are case sensitive. Invalid tags will throw a warning when the
build-site.py script is run.

## Formatting

- [Callout boxes](https://mmistakes.github.io/minimal-mistakes/docs/utility-classes/#notices)

## Acknolwedgments

Icons are from the [Prime icon set](https://icon-sets.iconify.design/prime/) from
Iconify. 