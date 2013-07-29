#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  scenario_gen.py
#  
#  Copyright 2013 Paul Lenton <lentonp@gmail.com>
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  
#  Maintenance notes:
#
#  Please note - unless otherwise stated, commented out lines are for
#  debugging
#
#  v1 released 12/02/2013 (UK date standard)
#  v2:
#  redesigned for a more complete look and feel
#  v2.1:
#  fixed a bug in a loop that wouldn't allow program to quit
#  v2.2:
#  Added a class to make easier referencing and tidier code in 
#  __main__
#  v2.3: 
#  Added a "scenarios" list and an option to choose how many scenarios 
#  will be used. 
#  Removed bug that stopped options printing in the event
#  of loop failure
#  v2.4:
#  Added try/except to handle value errors
#  Removed debugging code & TODO/FIXMEs

from random import randint
import time #entirely optional, if you don't like the sleep bits
			#you can remove any time.sleep() module

scenarioInt = 1
people = ["your Protaganist", "your Antagonist", "a minor character", "a major character"]
location = ["outdoors", "indoors", "in a motel", "in a hotel", 
	    "in a church"]
scenario = ["finds an old key to an unknown door", 
	    "is staring at their reflection in a mirror",
	    "has woken up hungover in a strange place",
	    "receives a disturbing phone-call",
	    "has just killed someone",
	    "is pacing back and forth, waiting for the phone to ring",
	    "has just evaded the police"]

class ScenarioGen(object):
	def __init__(self, person1, person2, scenario, location):
		self.person1 = person1
		self.person2 = person2
		self.scenario = scenario
		self.location = location
	
	def choosePerson1(self):
		"""Pick random person from list"""
		self.person1 = people[randint(0, len(people)-1)]
		return self.person1
		
	def choosePerson2(self):
		"""Pick another random person from the list"""
		# Make sure that the second person is not the same as the
		# first
		different_person = False
		while different_person is False:
			self.person2 = people[randint(0, len(people)-1)]
			if self.person2 != self.person1:
				# People differ
				different_person = True
				return self.person2
				

			
	def chooseScenario(self):
		"""Pick a random scenario from the list"""
		self.scen = scenario[randint(0, len(scenario)-1)]
		return self.scen
		
	def chooseLocation(self):
		"""Pick a random location from the list"""
		self.setting = location[randint(0, len(location)-1)]
		return self.setting

myScenario = ScenarioGen(1,2,3,4)
			
def printList(scenarioInt):
	"""Prints the output of the scenarioGen class"""
	print "Your scenario features %s and %s. \n" % (myScenario.choosePerson1(), myScenario.choosePerson2())
	print "The scenario is that a character %s, set %s.\n" % (myScenario.chooseScenario(), myScenario.chooseLocation())
	print "\n"
	print "Go again?"


def options():
	"""Prints options, repeated on a loop"""
	print "Here's your options... \n"
	print "1) Generate scenario"
	print "2) Exit."

def mainText():
	"""Print once, disregard"""
	print "Welcome to the Scenario generator. Please feel free",
	print "to change or add to the lists to make this a more",
	print "complete scenario generator for you. This version was",
	print "specifically built for my wife, Samantha Lenton."
	print "\n"


def main():
	"""Main body of program"""
	mainText()
	time.sleep(2)
	options()
	runLoop = ""
	while runLoop != "q": # If "q" then user wishes to quit
		input1 = raw_input("Choose 1 or 2: ")
		while input1 != 2:
			
			# ensure value selected is an integer (1 or 2) and allow
			# exceptions to avoid crashes
			try:
				int(input1) == (1 or 2)
			except ValueError:
				print "Sorry, I don't recognise that input\n"
				print "Please enter 1 or 2"
				break
			
			
			if int(input1) == 1:
				printList(int(scenarioInt))
				input2 = raw_input("Y/N: ")
				if input2.lower() == "no" or input2.lower() == "n":
					# Quit loop
					print "OK. Quitting"
					time.sleep(5)
					runLoop = "q"
					break
				elif input2.lower() == "yes" or input2.lower() == "y":
					# start integer selection loop again
					input1 = 1
				else:
					print "Sorry, I can only accept 'yes', 'y', 'no'",
					print "or 'n' as input."
					options()
					break
			elif int(input1) == 2:
				print "OK... quitting..."
				time.sleep(5)
				runLoop = "q"
				break
			else:
				# Input is neither 1 nor 2, restart loop with message
				print "Sorry I don't recognise that input\n"
				print "Please enter 1 or 2"
				break
		else:
			# Input == 2, user wishes to quit
			print "OK... quitting..."
			time.sleep(5)
			runLoop = "q" # break out of loop
			break
	return 0

if __name__ == '__main__':
	main()

