import sys
import os
import errno
import string

import tester

def validate_file(fin):
	import os.path
	base, ext = os.path.splitext(fin)
	if ext != '.fs19': 
		fin = fin + ".fs19" 
	try:
		with open(fin) as f:
			return fin
	except IOError as x:
		if x.errno == errno.ENOENT:
			print 'Error: Cannot find', fin
			print 'Exiting...', sys.argv[0] 
			sys.exit(1)
		elif x.errno == errno.EACCES:
			print 'Error: Cannot read', fin
			print 'Exiting...', sys.argv[0]
			sys.exit(1)
		elif x.errno == errno.EFBIG:
			print 'Error:', fin, ' too big'
			print 'Exiting...', sys.argv[0]
			sys.exit(1)

def usage_message():
	print "Error: Program invocation unaccepted."
	print "Please invoke using one of the three:"
	print "Usage: $[program]"
	print "Usage: $[program] [somefile]"
	print "Usage: $[program] < [somefile].fs19"

def main():

	if len(sys.argv) > 2:
		usage_message()
		sys.exit(2)
	if len(sys.argv) == 1:
		print 'Enter file data by keyboard input' 
		print '[Ctrl-D | Ctlr-Z + Enter] to save'
		print 'Disregard if invoking redirection'
		data = sys.stdin.read()
		try:
			with open('cin.fs19', 'w+') as f:
				f.write(data)
				cin = f.name
		except IOError as x:
			if x.errno == errno.EACCES:
				print 'Error: Cannot write file'
				print 'Exiting...', sys.argv[0]
				sys.exit(1) 				
		filename = validate_file(str(cin))
		tester.tester(filename)
	if len(sys.argv) == 2:
		filename = validate_file(str(sys.argv[1]))
		tester.tester(filename)
		
if __name__ == "__main__":
	main()
