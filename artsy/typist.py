'''Name: typist.py
Author: Sam Teeter
Description: 
A few functions for artsy text output effects.'''

import time, sys

def delay_write(c, delay=0.1):
	'''Writes one character to stdout, then waits 'delay' seconds and flushes
	the buffer.'''
	sys.stdout.write(c)
	time.sleep(delay)
	sys.stdout.flush()
	
def delay_print(s, delay=0.05):
	'''Prints s to stdout with 'delay' seconds between characters.'''
	for c in s:
		delay_write(c, delay)
	print
	
