#!/usr/bin/env python3

'''
	Here's how you upload an image. For this example, put the cutest picture
	of a kitten you can find in this script's folder and name it 'Kitten.jpg'
	For more details about images and the API see here:
		https://api.imgur.com/endpoints/image
'''

# Pull authentication from the auth example (see auth.py)
from auth import authenticate

from datetime import datetime
import os

album = None # You can also enter an album ID here

def upload_kitten(client):
	'''
		Upload a picture of a kitten. We don't ship one, so get creative!
	'''

	# Here's the metadata for the upload. All of these are optional, including
	# this config dict itself.
	config = {
		'album': album,
		'name':  '',
		'title': '',
		'description': ''
	}
	rootdir = "/home/matt/Desktop/melissa-pics-1"
	for subdir, dirs, files in os.walk(rootdir):
		print("Uploading image... ")
		for file in files:
			#print os.path.join(subdir, file)
			filepath = subdir + os.sep + file

			if filepath.endswith(".jpg"):
				print (filepath)
				image = client.upload_from_path(filepath, config=config, anon=False)
				print("Done")
				continue
			elif filepath.endswith(".jpeg"):
				print (filepath)
				image = client.upload_from_path(filepath, config=config, anon=False)
				print("Done")
				continue
			elif filepath.endswith(".png"):
				print (filepath)
				image = client.upload_from_path(filepath, config=config, anon=False)
				print("Done")
				continue
			elif filepath.endswith(".JPG"):
				print (filepath)
				image = client.upload_from_path(filepath, config=config, anon=False)
				print("Done")
				continue
			elif filepath.endswith(".JPEG"):
				print (filepath)
				image = client.upload_from_path(filepath, config=config, anon=False)
				print("Done")
				continue
			elif filepath.endswith(".PNG"):
				print (filepath)
				image = client.upload_from_path(filepath, config=config, anon=False)
				print("Done")
				continue
			else:
				print("not a picture")
				continue
			
	
	return image


# If you want to run this as a standalone script
if __name__ == "__main__":
	client = authenticate()
	image = upload_kitten(client)

	print("Image was posted! Go check your images")
	print("You can find it here: {0}".format(image['link']))
