from spiderer import spiderer
from time import strftime

journals = np.genfromtxt('journal_list.csv',
 delimiter = ';',
 dtype = 'str')

# Each list element is a journal
# Each element within that list follows the order
# 1. Last updated
# 2. Journal ID
# 3. Journal publisher
# 4. Journal full name

for i in range(0, len(x)):
	# Run the spiderer for the journal
	spiderer(journal = journals[i][1], publisher = journals[i][2])
	# Update the last update time
	journals[i][0] = strftime("%Y%m%d")

# This updates the last time the links have been generated
np.savetxt('journal_list.csv',
	journals,
	delimiter = ';',
	fmt = '%s')