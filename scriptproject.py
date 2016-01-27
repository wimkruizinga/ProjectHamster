#! /usr/bin/env python

from numpy import binary_repr
import numpy as np
#import os #maybe for the more files

#maybe import re to load regular expression module
import re

#Make a function for the decimals to binary conversion
def decbin(DecNum): 
	#Define the variable 'Bin' in which we will put the binary number of the input
	Bin=binary_repr(DecNum, width=8)
	
	#Define the variable BinInv which will contain the inverted binary number of Bin
	BinInv=""
	#This is done by making a for loop:	
	for bit in Bin:
		if bit == "0":
			BinInv += "1"
		else:
			BinInv += "0"
	
	return BinInv
#Finished defining the decbin function

#Define file name and give a name to the output file
InFileName = '201010100.txt'
OutFileName = InFileName + 'ScriptedTime.txt'

InFile = open(InFileName, 'r')
OutFile = open(OutFileName, 'w')

#loop through each line in the file
for Line in InFile:
	#Strip the line endings and white space
	Line=Line.strip()
	
	#Split by one more occurrence of a space
	ElementList = re.split(" +", Line)
	#print ElementList
	
	#Manier om data duidelijker te maken:
	Time=str(ElementList[0])+str(ElementList[1]).zfill(2)+ \
	str(ElementList[2]).zfill(2)+str(ElementList[3]).zfill(2)+ \
	str(ElementList[4]).zfill(2)+ str(ElementList[5]).zfill(2)+ \
	str(ElementList[6]).zfill(3)
	
	OutFile.write(Time + '\t')
	
	#for each column in the range of 7 until 13,
	for Column in range(7,13):
		#write the binary number in integer form, followed by an end-of-line in the OutFile
		OutFile.write(decbin(int(ElementList[Column])))
		#OutFile.write(int(decbin(int(ElementList[Column])))) ?
		
		#print the same output into the terminal
		#print decbin(int(ElementList[Column])),
	OutFile.write('\n')
	
print "Output printed to outfile"
	
#Close the files
InFile.close()
OutFile.close()

#Poging tot het maken van een list van de output van de vorige loop
OutFile = open(OutFileName, 'r')

OutFileName2= OutFileName + 'listig.txt'
OutFile2 = open(OutFileName2, 'w')

#This for loop is made to create a list which will contain all data for one day
#Which will contain an array for each

#Make a new list, named 'dag'
dag =list()
#for each line in OutFile
for line in OutFile:
	#Make a new list, named 'linelist'
	linelist= list()
	#Of each Line in OutFile, strip off the end-of-line signs
	line = line.strip('\n')
	# Split each line based on tabs
	# which gives two elements: the date/time column and the channel-output column
	# and put them into 'col'
	col = re.split("\t", line)
	#append the integer of the first element of 'col' (date/time) to the list 'linelist'
	linelist.append(int(col[0]))
	
	#make a new list named 'channel'
	channel = list()
	
	# for each character in col[1] (i) in range 0-47,
	# append the integer of it to the list 'channel'
	for i in range(0,47):
		channel.append(int(col[1][i]))
		
	# append the list 'channel' (3rd dimension) to the list 'linelist' (2nd dimension)
	linelist.append(channel)
	# append the list 'linelist' to the list 'dag' (1st dimension)
	dag.append(linelist)

#print the 3D list 'dag'	
lastevent=len(dag)-1
firstevent = dag[0][0]
TimeInterval=10000000
print dag[lastevent][0]	

#loop through each line of the file to write it to OutFile2:
for line in dag:
	OutFile2.write("%s\n" % line)



