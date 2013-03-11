import sys, os, zipfile

if len(sys.argv) < 2:
	print "Please enter a directory."
	sys.exit()

directory = sys.argv[1]

import os

if not os.access(directory, os.F_OK):
	print "Not a valid directory."
	sys.exit()

for(path, dirs, files) in os.walk(directory):
	for my_file in files:
		print "File: " + my_file

		#change filename to a zip filename
		if my_file.find(".mp3") != -1:
			zip_file = my_file.replace(".mp3", ".zip")
			print "Zip File: " + zip_file

			zip_me = zipfile.ZipFile(zip_file, "w")
			directory_zip = os.path.join(directory, os.path.basename(my_file))
			#print "Directory: " + directory_zip
			zip_me.write(my_file, my_file, zipfile.ZIP_DEFLATED)
			#zip_me.setpassword(password)
			zip_me.close()
