# Paleo Data Knowledge Hub

This repository contains files for the [Paleo Data Knowledge Hub](https://paleo-data.github.io/knowledge-hub) website, which enables open access to resources for anyone producing, managing, or utilizing paleontological specimen data. The hub empowers ongoing engagement and continuous knowledge sharing across stakeholder communities. Resources hosted on the knowledge hub are broadly relevant, and ideally adaptable to other domains beyond paleo. The site design strives to be human-centered, especially prioritizing an intuitive interface with a low barrier to entry for new users.

## Site structure

The site is organized primarily by collections.

### Community

### Data ecosystem

### Topics

#### Explanations

#### How To guides

#### Tutorials

### Resources

Items in the resources collection are created by querying the Zenodo API based on records in _data/zenodo.yml. To add a new resource, add a new entry to that file. Each entry must include a numeric Zenodo ID and can also include a list of tags.

### Tags

Pages in the tag collection are also generated automatically. Each page in the site can be assigned one or more tags using the tags variable in the front matter of the
source file. Tags are case sensitive. Invalid tags will throw a warning when the build-site.py script is run.

## Formatting

- [Callout boxes](https://mmistakes.github.io/minimal-mistakes/docs/utility-classes/#notices)

## Acknolwedgments

Icons are from the [Remix icon set](https://icon-sets.iconify.design/ri/) (Apache 2.0) from Iconify. 
