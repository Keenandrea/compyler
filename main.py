import sys
import os
import string

def fval(fin):
	fin = fin + ".fs19" 
	try:
		fp = open(fin)
		try:
			fp.read()
		except IOError:
			print "Error: Cannot read {}.".format(fp.name)
			fp.close()
		finally:
			print "{} read successfully...".format(fp.name)
			print "Closing {} handler...".format(fp.name)
			fp.close()
	except IOError:
		print "Error: Cannot find {}.".format(fin)
		print "Exiting {}...".format(sys.argv[0])
		sys.exit(1)
		
def main():

	if len(sys.argv) > 2:
		print "Error: Invocation of {} for {} is invalid.".format(str(sys.argv), sys.argv[0])
		print "Usage"
		sys.exit(2)
	if len(sys.argv) == 1:
		cin = str(raw_input())
		print cin
	if len(sys.argv) == 2:
		fval(str(sys.argv[1]))
		
if __name__ == "__main__":
	main()
