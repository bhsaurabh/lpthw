#!/usr/bin/python -tt
from sys import exit

def gold_room():
	print "This room is full of gold. How much do you take?"
	next = raw_input("> ")
	# if "0" in next or "1" in next:
	# 	how_much = int(next)
	# else:
	# 	dead("Man, learn to type a number.")
	try:
		how_much = int(next)
	except ValueError:
		dead("man, learn to type a number.")

	if how_much < 50:
		print "Nice, you are not greedy. You win!"
		exit(0)
	else:
		dead("You greedy bastard!")

def bear_room():
	print "There is a bear here."
	print "The bear has a bunch of honey."
	print "The fat bear is in front of another door."
	print "How are yu going to move the bear?"
	bear_moved = False

	while True:
		next = raw_input('> ')

		if 'honey' in next.lower():
			dead("The bear looks at you, then slaps your face off.")
		elif 'taunt' in next.lower() and not bear_moved:
			print "The bear has moved from the door. You can go through it now."
			bear_moved = True
		elif 'taunt' in next.lower() and bear_moved:
			dead("The bear gets pissed off and chews you leg off.")
		elif ('door' in next.lower() or 'open' in next.lower()) and bear_moved:
			gold_room()
		else:
			print "I got no idea what that means."

def cthulu_room():
	print "Here you see the great evil Cthulu."
	print "He, it, whatever stares at you and you go insane."
	print "Do you flee for your life or eat your head?"

	next = raw_input('> ')

	if "flee" in next:
		start()
	elif "head" in next:
		dead("Well! That was tasty.")
	else:
		cthulu_room()

def dead(why):
	print why, 'Good Job!'
	exit(0)

def start():
	print 'You are in a dark room.'
	print 'There is a door to your right and left.'
	print 'Which one do you take?'
	next = raw_input('> ')

	if next.lower() == 'left':
		bear_room()
	elif next.lower() == 'right':
		cthulu_room()
	else:
		dead('You stumble around the room until you starve.')

start()