'''

Script to prepare the data (select words corresponding only to a given year).
To be run before MostPopWords.py

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

#!/usr/bin/pyspark

import sys
import os
import shutil

from pyspark import SparkContext

if __name__ == "__main__":
	'''
		Usage (on a desktop): spark-submit prepareData.py
	'''

	sc = SparkContext(appName="MostPopWords")

	# data were taken from: https://storage.googleapis.com/books/ngrams/books/datasetsv2.html
	# here goes the folder with the data
	# REPLACE WITH YOUR DIRECTORY
	rawfiles = sc.textFile("/home/piotr/Downloads/NGRAMS_IT_UNPACKED")

	words = rawfiles.map(lambda line: line.split("\t"))
	words_2006 = words.filter(lambda line: "2006" in line[1])

	# save to txt file
	def toCSVLine(data):
		return '\t'.join(d for d in data)
	
	dir_name = "words_2006"
	
	# remove previous directory
	if (os.path.isdir(dir_name)):
		shutil.rmtree(dir_name)
	
	words_2006.map(toCSVLine).saveAsTextFile(dir_name)

