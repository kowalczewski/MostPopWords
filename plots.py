'''
This file includes function to prepare plots.

This file is part of MostPopWords.

MostPopWords is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.

'''

import numpy as np
import scipy.interpolate as interp
import matplotlib.pyplot as plt
import math
import sys

if __name__ == "__main__":
	
	"""
        	Usage: python plots.py
	"""

	word_count_filename = "word_count.out"

	# read JV characteristic
	percent_of_words = []
	no_of_words = []
	percent_of_usage = []
	with open(word_count_filename) as word_count_f:
		for line in word_count_f:
			line = line.split()
			percent_of_words.append(float(line[0]))
			no_of_words.append(float(line[1]))
			percent_of_usage.append(float(line[2]))

	plt.plot(no_of_words, percent_of_usage, linewidth=2)

	plt.xscale('log')
	
	plt.ylim(0,100)	

	plt.xlabel('Number of words (log scale)')
	plt.ylabel('Usage (%)')

	plt.show()
		
	
