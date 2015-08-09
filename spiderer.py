import numpy as np
import re
import
from get_links import process

# get all links from lvl1 (in an array)
lvl2_unselect = np.array(process(edit.lvl1))
# select only the lvl2 recognized links
r = re.compile(edit.lvl1_recog)
vmatch = np.vectorize(lambda x:bool(r.match(x)))
lvl2 = np.sort(lvl2_unselect[vmatch(lvl2_unselect)]) # make sure they are sorted

# create lvl3 object to append to
lvl3 = []
for link in lvl2:
	# get all links from lvl3 (in an array)
	lvl3_unselect = np.array(process(link))

	# select only the lvl3 recognized links
	r = re.compile(edit.lvl2_recog)
	vmatch = np.vectorize(lambda x:bool(r.match(x)))
	lvl3.append(np.sort(lvl3_unselect[vmatch(lvl3_unselect)]))

	print "Still working on lvl3 extraction, %s" % link

# fit all results of lvl3 into one array instead of multiple
lvl3 = np.concatenate(lvl3)

# create lvl3 object to append to
lvl4 = []
for link in lvl3:
	# get all links from lvl4 (in an array)
	lvl4_unselect = np.array(process(link))

	# select only the lvl3 recognized links
	r = re.compile(edit.lvl3_recog)
	vmatch = np.vectorize(lambda x:bool(r.match(x)))
	lvl4.append(np.sort(lvl4_unselect[vmatch(lvl4_unselect)]))

	print "Still working on lvl4 extraction, %s" % link

# fit all results of lvl4 into one array instead of multiple
lvl4 = np.concatenate(lvl4)

np.savetxt("journals/%s.csv" % edit.journal, lvl4, fmt = "%s")