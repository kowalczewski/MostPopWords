# Most Popular Words

## Description

Simple program showing how to use Spark and Python, and publicly available data to 
obtain the most popular words in a given language.

I consider Italian and use data from:
https://storage.googleapis.com/books/ngrams/books/datasetsv2.html

As an output, you should get:
1) The list of the most popular words in a given language (in a given year), and the number showing how many times they appeared.
2) Usage (in %) as a function of the number of words. It shows how "nonlinear" is the language (i.e., some words
are used much more often than others).

## How to run the code

What you need is Python (ver. 2.7) and Spark.

Be careful: when I use this code on my laptop, all 4 processors are 100% busy. Of course in Spark
you can adjust the number of nodes you are going to use.

1. Download the data. For example, from https://storage.googleapis.com/books/ngrams/books/datasetsv2.html.
2. Prepare a folder with unpacked data (only the data you are going to process, no unnecessary files).
3. Run prepareData.py script to extract words corresponding to a given year. The data will be saved in "words_2006" folder.
4. Run MostPopWords.py script. The results are saved in two files:
	1) italian_top100.out (most popular words)
	2) word_count.out (usage as a function of the number of words)
5. You can plot the data form word_count.out file using plots.py script.

The default plot shows usage (in %) as a function of the number of words. 
The plot should tell something like: "If I know 100 words in Italian, 
I should understand around 20% of the text". (very roughly)

## Additional remarks

The analysis also depends on the parameters you use. E.g., the threshold -- 
do not include words with counts below a certain threshold (e.g., very technical).

Depending on the threshold, the number of words in a given language can be very large.

## Disclaimer

This was just a hobby problem (I am currently learning Spark). Having said that, 
I am not doing any serious research related to language etc. It is definitely 
not a serious scientific analysis, it may contain flaws etc. 
Still I find it quite interesting. Nevertheless, I feel obligated to write this disclaimer:

The author does not make any warranty, expressed or implied, or assume any legal liability or 
responsibility for the accuracy, completeness or usefulness of any information contained in this work. 
Use the information and instructions contained in this work at your own risk.

## LICENSE

License: GNU General Public License v3.0 (see: LICENSE file)

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
