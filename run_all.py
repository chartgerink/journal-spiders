from spiderer import spiderer

journals = np.genfromtxt('journal_list.csv',
 delimiter = ';',
 skiprows = 1,
 dtype = 'str')

# Each list element is a journal
# Each element within that list follows the order
# 1. Last updated
# 2. 



# This updates the last time the links have been generated
np.savetxt('journal_list.csv',
	journals,
	delimiter = ';',
	fmt = '%s')