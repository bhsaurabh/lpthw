#!/usr/bin/python -tt
x = "There are %d types of people." % 10 # assignment
binary = "binary"
do_not = "don't"
y = "Those who know %s and those who %s" % (binary,do_not)

print x
print y

print "I said: %r" % x # print raw string i.e. with quotes
print "I also said: %s" % y # print string without quotes

hilarious = False
joke_evaluation = "Isn't that joke funny?! %r"

print joke_evaluation % hilarious

w = "This is the left side of..."
e = "a string with a right side."
print w+e