from spiderer import spiderer
from time import strftime
from datetime import datetime
import numpy as np

donotrun_days = 7

journals = np.genfromtxt('journal_list.csv',
 delimiter = ';',
 dtype = 'str')

# Each list element is a journal
# Each element within that list follows the order
# 1. Last updated
# 2. Journal ID
# 3. Journal publisher
# 4. Journal full name
# 5. Selection variable (1 = run; 0 = no run)

current = datetime.strptime(strftime('%Y%m%d'), '%Y%m%d')

for i in range(0, len(journals)):
	if journals[i][4] == '1':
		if not not journals[i][0]:
			last = datetime.strptime(journals[i][0], '%Y%m%d')

			days = current - last

			if days.days > donotrun_days:
				# Run the spiderer for the journal
				spiderer(journal = journals[i][1], publisher = journals[i][2])
				# Update the last update time
				journals[i][0] = strftime("%Y%m%d")

				# This updates the last time the links have been generated
				np.savetxt('journal_list.csv',
					journals,
					delimiter = ';',
					fmt = '%s')
		else:
			# Run the spiderer for the journal
			spiderer(journal = journals[i][1], publisher = journals[i][2])
			# Update the last update time
			journals[i][0] = strftime("%Y%m%d")

			# This updates the last time the links have been generated
			np.savetxt('journal_list.csv',
				journals,
				delimiter = ';',
				fmt = '%s')

	print 'Running... Currently at iteration %s of %s' % (i, len(journals))