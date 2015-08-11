def spiderer(journal, publisher):
	if publisher == 'sage':
		sage(journal = journal)

def springer(journal):
	import numpy as np
	import re
	from get_links import process

	# lvl1 is the base url
	lvl1 = 'http://link.springer.com/journal/volumesAndIssues/%s' % journal

	# links to recognize at lvl1 for lvl2
	lvl1_recog = 'http://link.springer.com/journal/[0-9]{1,}/[0-9]{1,}/[0-9]{1,}/page/[0-9]{1,}'
	# links to recognize at lvl2 for lvl3
	lvl2_recog = 'http://link\.springer\.com/article/[0-9]{2}\.[0-9]{4}/(?!.*fulltext\.html$).*'

	# get all links from lvl1 (in an array)
	lvl2_unselect = np.array(process(lvl1))
	# select only the lvl2 recognized links
	r = re.compile(lvl1_recog)
	vmatch = np.vectorize(lambda x:bool(r.match(x)))
	lvl2 = np.sort(lvl2_unselect[vmatch(lvl2_unselect)]) # make sure they are sorted

	# create lvl3 object to append to
	lvl3 = []
	for link in lvl2:
		# get all links from lvl3 (in an array)
		lvl3_unselect = np.array(process(link))
	
		# select only the lvl3 recognized links
		r = re.compile(lvl2_recog)
		vmatch = np.vectorize(lambda x:bool(r.match(x)))
		lvl3.append(np.sort(lvl3_unselect[vmatch(lvl3_unselect)]))

		i = 1
		x = "continue"
		while x == "continue":
			s = list(link)
			s[-1] = str(i + 1)
			link = "".join(s)

			lvl3_unselect = np.array(process(link))
	
			# select only the lvl3 recognized links
			r = re.compile(lvl2_recog)
			vmatch = np.vectorize(lambda x:bool(r.match(x)))
			temp = np.sort(lvl3_unselect[vmatch(lvl3_unselect)])

			if temp.size == 0:
				x = "stop"

			if x == "continue":
				lvl3.append(temp)

			i += 1

		print "Still working on lvl3 extraction, %s" % link

	# fit all results of lvl3 into one array instead of multiple
	lvl3 = np.concatenate(lvl3)

	np.savetxt("journals/springer_%s.csv" % journal, lvl3, fmt = "%s")


def sage(journal):
	import numpy as np
	import re
	from get_links import process
	# lvl1 is the base url
	lvl1 = 'http://%s.sagepub.com/content/by/year/' % journal
	
	# links to recognize at lvl1 for lvl2
	lvl1_recog = 'http://%s.sagepub.com/content/by/year/[0-9]{4}' % journal
	# links to recognize at lvl2 for lvl3
	lvl2_recog = 'http://%s.sagepub.com/content/vol[0-9]{1,}/issue[0-9]{1,}/' % journal
	# links to recognize at lvl3 for lvl4
	lvl3_recog = 'http://%s.sagepub.com/content/[0-9]{1,}/[0-9]{1,}/[0-9]{1,}.full.pdf+html' % journal

	# get all links from lvl1 (in an array)
	lvl2_unselect = np.array(process(lvl1))
	# select only the lvl2 recognized links
	r = re.compile(lvl1_recog)
	vmatch = np.vectorize(lambda x:bool(r.match(x)))
	lvl2 = np.sort(lvl2_unselect[vmatch(lvl2_unselect)]) # make sure they are sorted
	
	# create lvl3 object to append to
	lvl3 = []
	for link in lvl2:
		# get all links from lvl3 (in an array)
		lvl3_unselect = np.array(process(link))
	
		# select only the lvl3 recognized links
		r = re.compile(lvl2_recog)
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
		r = re.compile(lvl3_recog)
		vmatch = np.vectorize(lambda x:bool(r.match(x)))
		lvl4.append(np.sort(lvl4_unselect[vmatch(lvl4_unselect)]))
		
		print "Still working on lvl4 extraction, %s" % link
	
	# fit all results of lvl4 into one array instead of multiple
	lvl4 = np.concatenate(lvl4)
	
	np.savetxt("journals/sage_%s.csv" % journal, lvl4, fmt = "%s")