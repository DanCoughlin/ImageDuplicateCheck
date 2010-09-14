#!/Library/Frameworks/Python.framework/Versions/Current/bin/python

#	author: dan coughlin
#	date: 2010-09-14
#	file: checkdupe.py
#	purpose: this script will check a directory 
#	for duplicate images.  If a duplicate image
#	is found, it will spit out the names of 
#	both images.  This does not do recursive 
#	directory traversing, it only checks the directory
#	given
#
#	example: 
#	./checkdupe.py /path/to/directory/
#	example if directory has spaces:
#	./checkdup.py "/path/to directory/with spaces"
#






import sys
import Image
import os,glob

"""
this function takes two image files and 
compares them to see if they are the same
both arguments expect to be created from
the result of: Image.open(/path/to/image.ext).getdata()
"""
def is_the_same(base, test_image):
	for i in range(len(base)):
		for j in range(len(base[i])):
			# as soon as we find any difference, the images
			# don't match
			if (base[i][j] - test_image[i][j]) != 0:
				return False
	return True


"""
this function ensures that the arguments passed to the script are ok
and if not will exit the program before we try to use them
"""
def validate_args(script_args):
	if len(script_args) != 2:
		example_call()
		sys.exit()


"""
this function will display an example of the proper
way to call this script
"""
def example_call():
		print "You did not call this script properly."
		print "Examples (note use of quotes if spaces in directory path):"
		print "./checkdupe.py /path/to/directory/to/check"
		print "./checkdupe.py \"/path/to/directory with spaces/to/check\"\n"


"""
check_images takes a path to a directory and checks
each file against each other to determine if
there are any duplicates.  If so, paths to both
files are printed
"""
def check_images(path):
		index = 0
		myfiles = glob.glob( os.path.join(path, '*.*'))
		# loop over files in directory to look at
		for infile in myfiles: 
			index += 1 
			# get base file to compare against the rest
			base = Image.open(infile).getdata()
			# get lis of files to compare against base file
			# assume we have checked the previous files in 
			# the myfiles listing (for example no need to check
			# if image 2 is the same as image 1, we have already 
			# tested if image 1 is the same as image 2 (don't check again)
			complist = myfiles[index:]
			# loop over the rest of the files that haven't been checked as 
			# the base file yet
			for comp in complist:
				check = Image.open(comp).getdata()
				# determine if two files are the same
				status = is_the_same(base, check)
				if status:
					print "Duplicate:"
					print infile
					print "%s\n" %comp


def main():

	validate_args(sys.argv)
	path = sys.argv[1]

	if os.path.isdir(path):
		print "Checking for duplicate images in:\n%s\n" % path 
		check_images(path)
	else:
		print "%s is not a directory" % path 

	print "done."


if __name__ == '__main__':
	main()
