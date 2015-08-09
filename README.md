# journal-spider: facilitating the spidering of journal articles to scrape
---
The ContentMine facilitates scraping journals, via both [`getpapers`](), [`quickscrape`](), and [`journal-scrapers`](), but finding the links to input into `quickscrape` remains a tedious job if done manually. This repository provides a way of spidering journals which requires only minimal user adjustment.

Note: this is currently being made based on the SAGE journal layout, as presented in Psychological Science. Cross-testing within SAGE has been done for Perspectives on Psychological Science and Personality and Social Psychology Review. Other publishers will be added later

The main workhorse, [`get_links.py`](https://github.com/jabbalaci/Bash-Utils/blob/master/get_links.py) was written by Laszlo Szathmary in 2011. This file returns all links on a webpage, which is all we really need. What needs to be done manually is K-folded:

1. Edit the `edit.py` file according to your journal (SAGE only for now). Typically, only the part prior to `.sagepub.com/...` has to be edited and the journal name (note: journal is also the name for which the file will be written)
2. Run `spiderer.py`
3. Wait.