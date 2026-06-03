# By Timothy Edmonds

import numpy as np
import math
import matplotlib.pyplot as plt
import fractions as fr

def num_cap(n, C):
	if n == 1:
		all_caps = [[fr.Fraction(C, 1)]]
	elif n != 1:
		all_caps = num_cap(n-1, C)
		new_caps = []
		for ii in range(1,math.ceil(n/2)+1):
			c_parr = [(c1+c2) for c1 in all_caps[ii-1] for c2 in all_caps[n-1-ii]]
			c_seri = [c1*c2/(c1+c2) for c1 in all_caps[ii-1] for c2 in all_caps[n-1-ii]]
			new_caps.extend(c_parr)
			new_caps.extend(c_seri)
		new_caps = list(set(new_caps))
		all_caps.append(new_caps)
		
	return all_caps


# for jj in range(6,7):
	# num_caps = jj
	# n_tested = 10000000
	# C_range = np.linspace(1,n_tested,n_tested)
	# C_unique = np.zeros(np.shape(C_range))
		
	# for ii in range(n_tested):
		# C = C_range[ii]
		# all_caps = num_cap(num_caps, C)
		# caps = [x for caps in all_caps for x in caps]
		# caps = list(set(caps))
		# C_unique[ii] = len(caps)
		
	# C_best = np.argmax(C_unique) + 1
	# print(C_best)

all_caps = num_cap(18, 1)
caps = [x for caps in all_caps for x in caps]
caps = list(set(caps))
print(len(caps))
	
#plt.plot(C_range, C_unique)
#plt.xlabel("Value of each capacitor in circuit")
#plt.ylabel("Number of Unique capacatince circuits")
#plt.show()