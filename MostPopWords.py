'''
MostPopWords

Simple program showing how to use Spark and Python, and publicly available data to 
obtain the most popular words in a given language.

This program is free software: you can redistribute it and/or modify
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
import numpy

from pyspark import SparkContext

if __name__ == "__main__":
	'''
		Usage (on a desktop): spark-submit MostPopWords.py
	'''

        sc = SparkContext(appName="MostPopWords")

	# data were taken from: https://storage.googleapis.com/books/ngrams/books/datasetsv2.html
	# here goes the folder with the data (data are prepared using prepareData.py script)
	# REPLACE WITH YOUR DIRECTORY
	words = sc.textFile("/home/piotr/Downloads/words_2006").map(lambda line: line.split("\t"))

	# take words longer than min_length (chars)
	min_length = 3
	# threshold -- do not include words with counts below a certain threshold (e.g., very technical)
	word_count_threshold = 100	
	# convert from str to int, remove unnecessary columns
        words_filtered = words.filter(lambda keyValue: len(keyValue[0]) > min_length).filter(lambda line: "_" not in line[0]).map(lambda line: ( line[0], int(line[2]))).filter(lambda line: line[1] > word_count_threshold)

        # add indices (for the analysis below)
        words_sorted = words_filtered.sortBy(lambda x: x[1], ascending=False)
        words_sorted.cache()

        # how many words
        tot_words = float(words_sorted.count())
        # how many counts
        tot_count = words_sorted.reduce(lambda x,y: (0, x[1]+y[1]))[1]

        fraction_vec = numpy.logspace(-4,0,20)

	out_f = open("word_count.out","w")

        for fraction in fraction_vec:
		# take fraction of words
		# at the end: remove indices
		words_frac = words_sorted.zipWithIndex().filter(lambda line: line[1]<=fraction*float(tot_words)).map(lambda line: line[0] )

                # sum the counts in a given fraction
                counts_frac = words_frac.reduce(lambda x,y: (0, x[1]+y[1] ) )[1]
		
		# percent of words, number of words, percent of usage
		print>>out_f, fraction*100, int(fraction * tot_words), float(counts_frac)/float(tot_count)*100

	out_f.close()
				
        # print the top 100 words
        out_f = open("italian_top100.out","w")
        top = words_sorted.take(100)
        for line in top:
                print>>out_f, line[0].encode('utf-8'), line[1]
        out_f.close()

		
