# journal-spider: facilitating the spidering of journal articles to scrape
---
The ContentMine facilitates scraping journals, via both [`getpapers`](), [`quickscrape`](), and [`journal-scrapers`](), but finding the links to input into `quickscrape` remains a tedious job if done manually. This repository provides a way of spidering journals which requires only minimal user adjustment.

Note: this is currently being made based on the SAGE journal layout, as presented in Psychological Science. Cross-testing will apply only later.

The main workhorse, [`get_links.py`](https://github.com/jabbalaci/Bash-Utils/blob/master/get_links.py) was written by Laszlo Szathmary in 2011. This file returns all links on a webpage, which is all we really need. What needs to be done manually is K-folded:

1. Set the base url.
2. 