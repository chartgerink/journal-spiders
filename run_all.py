from spiderer import spiderer
from time import strftime
from time import sleep
from datetime import datetime
import numpy as np

donotrun_days = 7

journals = np.genfromtxt('journal_list.csv',
 delimiter = ',',
 dtype = 'str')

# Each list element is a journal
# Each element within that list follows the order
# 1. Last updated
# 2. Journal ID
# 3. Journal publisher
# 4. Journal full name
# 5. Selection variable (1 = run; 0 = no run)
# 6. Field
	
# Ensure a random ordering of the array to prevent publisher recurrence
np.random.shuffle(journals)

# Create a vector of values with days since last run
current = datetime.strptime(strftime('%Y%m%d'), '%Y%m%d')
rundays = []
for i in xrange(0, len(journals[:,0])):
	try:
		last = datetime.strptime(journals[i][0], '%Y%m%d')
		days = current - last
	
		rundays.append(days.days)
	except ValueError:
		rundays.append('0')

# Loop through all journals, if not collected yet and 
while any(journals.T[0][journals.T[4] == '1'] == '') or rundays > donotrun_days:
	for i in range(0, len(journals)):
		if journals[i][4] == '1':
			if not not journals[i][0]:
				if rundays[i] > donotrun_days:
					try:
						# Run the spiderer for the journal
						spiderer(journal = journals[i][1], publisher = journals[i][2])
						# Update the last update time
						journals[i][0] = strftime("%Y%m%d")
		
						# This updates the last time the links have been generated
						np.savetxt('journal_list.csv',
							journals,
							delimiter = ',',
							fmt = '%s')
					except (TypeError, IndexError):
						pass
					except ValueError:
						journals[i][4] = '0'

						np.savetxt('journal_list.csv',
							journals,
							delimiter = ',',
							fmt = '%s')
					except IOError:
						sleep(np.random.poisson(60))
			else:
				try:
					# Run the spiderer for the journal
					spiderer(journal = journals[i][1], publisher = journals[i][2])
					# Update the last update time
					journals[i][0] = strftime("%Y%m%d")
	
					# This updates the last time the links have been generated
					np.savetxt('journal_list.csv',
						journals,
						delimiter = ',',
						fmt = '%s')
				except (TypeError, IndexError):
						pass
				except ValueError:
						journals[i][4] = '0'

						np.savetxt('journal_list.csv',
							journals,
							delimiter = ',',
							fmt = '%s')
				except IOError:
						sleep(np.random.poisson(60))
	
		sleep(np.random.poisson(3))
		print 'Running... Currently at iteration %s of %s' % (i + 1, len(journals))
