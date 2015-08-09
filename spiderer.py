import numpy as np
import re
from get_links import process

# lvl1 is the base url
lvl1 = 'http://pss.sagepub.com/'
# links to recognize at lvl1
lvl1_recog = 'http://pss.sagepub.com/content/by/year/[0-9]{4}'

# get all links from lvl1 (in an array)
links_lvl1_unselect = np.array(process(lvl1))

# select only the lvl1 recognized links
r = re.compile(lvl1_recog)
vmatch = np.vectorize(lambda x:bool(r.match(x)))
links_lvl1_select = np.sort(x[vmatch(x)]) # make sure they are sorted



