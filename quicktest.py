#!/Library/Frameworks/Python.framework/Versions/Current/bin/python

import sys
import Image
import os,glob

def is_the_same(base, test_image):
	for i in range(len(base)):
		for j in range(len(base[i])):
			if (base[i][j] - test_image[i][j]) != 0:
				return False
	return True

def main():
	base = Image.open('Picture-1.png').getdata()
	bad = Image.open('Picture-2.png').getdata()
	badder = Image.open('Picture-3.png').getdata()
	good = Image.open('Picture-4.png').getdata()

	#print is_the_same(base, bad) # returns True
	#print is_the_same(base, badder) # returns True
	print is_the_same(base, good) # returns False
	#a = Image.open('Picture-1.png')
	#b = Image.open('Picture-2.png')
	#print a.tostring()
	#print b.tostring()
	#path = "/Users/dmc186/Pictures/iPhoto\ Library/Data/iPhotoOriginals/2003/Orange\ Bowl\ 2006/"
	path = "/Users/dmc186/Pictures/iPhoto Library/Data/2003/Orange Bowl 2006"

	if os.path.isdir(path):
		print "path yo"
		index = 0
		myfiles = glob.glob( os.path.join(path, '*.*'))
		#for infile in glob.glob( os.path.join(path, '*.*') ):
		for infile in myfiles: 
			index += 1 
			base = Image.open(infile).getdata()
			complist = myfiles[index:]
			for comp in complist:
				check = Image.open(comp).getdata()
				status = is_the_same(base, check)
				if status:
					print "-------------------------------------------"
					print infile
					print comp
					print "-------------------------------------------"

	else:
		print "fail."
	print "done."

if __name__ == '__main__':
	main()
