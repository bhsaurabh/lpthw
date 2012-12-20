#!/usr/bin/python -tt
# import argv from sys module for command line parameters
from sys import argv
# unpack argv 
script, filename = argv
# open file specified by filename. Get a file objects with methods associated with it
txt = open(filename)

print "Here's your file %r:", filename
# use read() method of file object without any parameters
print txt.read()
txt.close()

print "\nI'll also ask you to type it again:"
file_again = raw_input('> ')

txt_again = open(file_again)
print txt_again.read()
txt_again.close()