# Paleo Data Knowledge Hub

This repository contains files for the [Paleo Data Knowledge Hub](https://paleo-data.github.io/knowledge-hub) website, which is a [Jekyll](https://jekyllrb.com/) site hosted by [GitHub Pages](https://pages.github.com/) and using the [Minimal Mistakes theme](https://github.com/mmistakes/minimal-mistakes).

> [!IMPORTANT]  
> _This readme describes the technical process for contributing, and is complemented by [this TBD description of the accompanying social process](), as well as [this TBD content style guide]()_.

## Licensing

The code for this site is provided freely under The MIT License (MIT), while the content contained within the [collections](/collections) directory is provided under a [CC 4.0 BY license](https://creativecommons.org/licenses/by/4.0/).

## Site design

_[TBD description of some technical design, including directory structure in this repo]_

## How to contribute to content

Site content is written in Markdown and resource metadata is written in YAML. Where resources are hosted on Zenodo, some metadata is pulled automatically from Zenodo. Most users do not have write access to this repository, so you will need to fork this repo by clicking on the <img width="85.2" height="20.4" alt="Screenshot 2025-07-31 at 12 25 28" src="https://github.com/user-attachments/assets/925a292c-5c8b-413b-b0a2-d420c397f139" />
 button and follow the steps below in your own fork. Learn more about [forking on GitHub here](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/working-with-forks/fork-a-repo).

### Edit an existing page

#### Step 1. Find the file

_[TBD content]_

#### Step 2. Make edits

_[TBD content]_

#### Step 3. Update page metadata

_[TBD content]_

#### Step 4. 

### Add a new page

See also [TBD social process]().

#### Step 1. Create the file

Create a Markdown file in the appropriate subdirectory of [collections](/collections). Filename should be lowercase and include only numbers, letters, and hyphens (as a word separator). It should exactly or closely match the page title and use the file extension `.md`. Follow conventions set by existing filenames in the directory.

#### Step 2. Include front matter

Open the Markdown file you just created and add the [front matter](https://jekyllrb.com/docs/front-matter/), which is a special section at the top of each Markdown document with metadata about the page that Jekyll uses to build the site. Front matter is delineated by a line of three hyphens before and after the content. The content itself consists of key-value pairs written in YAML, a human-readable markup language.

The front matter should include:

- The `title` of the page
- Associated `topics` formatted as a list that is comma-delimited within square brackets. Topics must come from [this TBD site-wide list]().
- The publication `status` of the page. Pages with `status: published` are considered complete. Pages with any other value will include a visual warning that the
  page is still in draft form, and will not appear in the site navigation. Draft pages can still be viewed on the site by entering the direct URL, e.g. "https://paleo-data.github.io/knowledge-hub/how-to-guides/capture-inventory-data" for a file named `capture-inventory-data.md` in the how-to guides collection.
- A list of `contributors` comma-delimited within square brackets. Contributors include any individuals who have added or edited content to the page. This list is comprehensive, i.e. names should only be added, never deleted.
- A `last_modified_at` date, formatted as `YYYY-MM-DD`. For new pages, this should be the date the file was created.

Metadata for the file [treatise-ip.md](/collections/_data-ecosystem/treatise-ip.md) might look like this:

```yaml
---
title: Treatise on Invertebrate Paleontology
topics: [treatise ip, taxonomy]
status: published
contributors: ["Jane Doe", "John Johnson"]
last_modified_at: 2025-07-21
---
```

Additional YAML metadata (for example, related to page layouts and navigation) are added automatically based on the collection the page appears in.

## How to write content

> [!IMPORTANT]  
> _See also [this TBD content style guide]()_.

Content is written in Markdown, which is a simple, readable syntax used to format text documents. Write all content below the front matter. See this handy [cheat sheet for Markdown](https://www.markdownguide.org/cheat-sheet/). Markdown files can also include HTML, but HTML should be used sparingly and only when suitable Markdown is not available, e.g. for embed tags.

Jekyll also supports [Liquid](https://shopify.github.io/liquid/), which is a template language that can be used to add dynamic content to pages. Liquid tags should also be used sparingly, with the primary exceptions being (1) use of the `relative_url` filter to link to pages elsewhere on the site and (2) use of `include` tags to display widgets defined by either the Minimal Mistakes template or created specifically for this site. Each of these situations is described in more detail below.

### Link within the site

Use Jekyll's `relative_url` filter to link to other pages on the site. This filter accepts a root-relative URL. Note that the collections directory is not part of the URL for pages in a collection and that page names do not need to include a file extension.

For example, to link a page in a collection, e.g. the file located at `[collections/_community/pdwg-happy-hours.md](collections/_community/pdwg-happy-hours.md)`: 

```
[PDWG Happy Hours]{{ "/community/pdwg-happy-hours" | relative_url }}
```

You can also link to a top-level page, i.e. a collection:

```
[Community]{{ "/community" | relative_url }}
```

### Use widgets to format types of content

Include a 
[callout box](https://mmistakes.github.io/minimal-mistakes/docs/utility-classes/#notices):

```
{: .notice--info }
This type of notice is used for sidebar information.
```

```
{: .notice--primary }
This type of notice is used for ...
```

```
{: .notice--warning }
This type of notice is used for ...
```

```
{: .notice--danger }
This type of notice is used for ...
```

Embed a Google Slide deck, for example:
```
<iframe src="https://docs.google.com/presentation/d/1yJFsaCnBC28zW8UtLfl3tnJayk3w-BRDtVzyZYpD1TI/embed?start=false&loop=false&delayms=10000" frameborder="0" width="480" height="299" allowfullscreen="true" mozallowfullscreen="true" webkitallowfullscreen="true"></iframe>
```

Embed a PDF hosted on Google Drive, for example:
```
<iframe src="https://drive.google.com/file/d/1aK_8LZoIgt6qETTHpbH_ZOjMRT7pghKX/preview" width="640" height="480" allow="autoplay"></iframe>
```

#### Add widgets to pull in content

Include a list of related pages matching one or more topics:

```
{% include related_list topics='manage data|share data' %}
```

Include a list of external resources defined in the [_data/resources](_data/resources) directory matching one or more topics:

```
{% include resource_list topics='symbiota' %}
```

Include a resource card to highlight a single resource defined in the [_data/resources](_data/resources) directory:

```
{% include resource_card filename='pearson-2022.yml' %}
```

## How to create and reference external resources

Information from external resources, like publications or websites, can also be included on the site. Resources are defined as YAML files in the `_data/resources` directory. Two templates for defining resources are available in the `templates/data` folder:

- `data-file-zenodo.yml` can be used for resources published on Zenodo. It includes only the metadata fields needed to identify and annotate a resource. Additional metadata is pulled from Zenodo when the site is built.
- `data-file-manual.yml` is intended for non-Zenodo resources (like websites) and includes the metadata fields needed to construct a complete reference.

Both files include the topics field, which can be used to tag the resources in the same way that internal pages are tagged.

## How to build the site

It can be useful to build the site locally before submitting a pull request or committing changes to the main repository. The build process uses a combination of Python and Ruby to index the site, update metadata for external resources, and build the HTML pages from the Markdown files.

Note that files created during the build process are not committed to GitHub. The build process runs automatically through a GitHub Action when changes are pushed to the repository.

### Do initial setup

Building the site locally requires that the following three applications are installed:

- [Git](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)
- [MiniForge](https://github.com/conda-forge/miniforge) (under Install)
- [Ruby](https://www.ruby-lang.org/en/downloads) (under Ways of Installing Ruby)

Once those applications are installed, you can [fork this repository](https://github.com/paleo-data/knowledge-hub/fork), then clone the fork to your system:

```
git clone https://github.com/{username}/knowledge-hub
```

Navigate to the directory you just created:

```
cd path/to/knowledge-hub
```

Set up the Python environment:

```
mamba create -f environment.yml
```

Set up Jekyll:

```
gem install bundler jekyll
```

### Build the site locally

Open the command prompt and run the following commands to activate the environment needed to build and run the site locally:

```
mamba activate pdh
cd path/to/knowledge-hub
```

To build the site and launch Jekyll, run the following commands in the same prompt:

```
cd scripts
python build-site.py
cd ..
bundle exec jekyll serve
```

Alternatively you can simply run Jekyll itself:

```
bundle exec jekyll serve
```

Jekyll will pick up many routine changes as files are updated, but some changes (including but not limited to changes to _config.yml or topic lists on individual
pages) will not be reflected until Jekyll is restarted or the full site is rebuilt.

## Acknowledgments

Icons are from the [Remix icon set](https://icon-sets.iconify.design/ri/) (Apache 2.0) from Iconify. 
