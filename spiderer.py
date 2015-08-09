import numpy as np
import re
from get_links import process

# lvl1 is the base url
lvl1 = 'http://pss.sagepub.com/content/by/year/'
# links to recognize at lvl1 for lvl2
lvl1_recog = 'http://pss.sagepub.com/content/by/year/[0-9]{4}'

# links to recognize at lvl2 for lvl3
lvl2_recog = 'http://pss.sagepub.com/content/vol[0-9]{1-3}/issue[0-9]{1-2}/'

# get all links from lvl1 (in an array)
lvl2_unselect = np.array(process(lvl1))

# select only the lvl1 recognized links
# these are lvl2 links
r = re.compile(lvl1_recog)
vmatch = np.vectorize(lambda x:bool(r.match(x)))
lvl2 = np.sort(lvl2_unselect[vmatch(lvl2_unselect)]) # make sure they are sorted

# create lvl3 object to append to
lvl3 = []

for link in lvl2:
	# get all links from lvl1 (in an array)
	lvl3_unselect = np.array(process(link))

	# select only the lvl2 recognized links
	# these are lvl3 links
	r = re.compile(lvl2_recog)
	vmatch = np.vectorize(lambda x:bool(r.match(x)))
	lvl3.append(np.sort(lvl3_unselect[vmatch(lvl3_unselect)]))