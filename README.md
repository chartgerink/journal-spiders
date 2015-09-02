# journal-spider: facilitating the spidering of journal articles to scrape
---
The ContentMine facilitates scraping journals, via both [`getpapers`](https://github.com/ContentMine/getpapers), [`quickscrape`](https://github.com/ContentMine/quickscrape), and [`journal-scrapers`](https://github.com/ContentMine/journal-scrapers), but finding the links to input into `quickscrape` remains a tedious job if done manually. This repository provides a way of spidering journals which requires only minimal user adjustment.

The main workhorse, [`get_links.py`](https://github.com/jabbalaci/Bash-Utils/blob/master/get_links.py) was written by Laszlo Szathmary in 2011. This file returns all links on a webpage, which is all we really need. Link extraction currently works for SAGE journals and Springer journals. In order to run this:

1. Import `spiderer` as module into python (make sure to have installed the `BeautifulSoup` module! `pip install BeautifulSoup` to do this)
2. Run `spiderer.sage(journal = '')` or `spiderer.springer(journal = '')` to download all links for that specific journal. For the `spiderer.sage()` you only need the first three letters of the web url (e.g., `pss` for [Psychological Science](pss.sagepub.com)); for `springer()` you require the unique journal identifier (e.g., 13428 for [Behavior Research Methods](http://link.springer.com/journal/volumesAndIssues/13428)); for `elsevier()` you require the unique journal identifier (e.g., 2212683X for [Biologically Inspired Cognitive Architectures](http://www.sciencedirect.com/science/journal/2212683X)).

If you want to collect the links for all journals available in `journal_list.csv`, you only need to use the command `python run_all.py` in the commandline of your choosing.

# To-do

- [x] Incorporate some form of selection mechanism into the journal_list
- [x] Incorporate a date checker to prevent re-spidering of recently spidered journals (what is a reasonable timeframe for this?)
- [x] Incorporate Elsevier
- [ ] Incorporate Taylor & Francis
- [ ] Incorporate Wiley
